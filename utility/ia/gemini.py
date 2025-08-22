import os
import google.generativeai as genai
from typing import List, Dict, Any, Optional
import json
from dotenv import load_dotenv

from .base_ia import IA, IAMessage, IAResponse
from dto import IANames

load_dotenv()

GEMINI_IA_NAME = "gemini"

class GeminiIA(IA):
    """
    Implementación de Gemini que hereda de la clase base IA
    
    Esta clase cumple con el principio LSP (Liskov Substitution Principle):
    - Mantiene las precondiciones y postcondiciones de la clase base
    - Puede sustituir a la clase base sin romper la funcionalidad
    - No fortalece las precondiciones ni debilita las postcondiciones
    """

    def get_ia_name(self) -> str:
        return IANames.GEMINI.value
    
    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None):
        """
        Inicializa el servicio de Gemini
        
        Args:
            api_key: API key de Google Gemini (opcional si está en variables de entorno)
            model_name: Nombre del modelo a usar (por defecto gemini-1.5-flash)
        """
        # Establecer el modelo por defecto si no se proporciona
        if model_name is None:
            model_name = self.default_model
        
        if api_key is None:
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise ValueError(
                    "API key no encontrada. Proporciona una API key o "
                    "configura la variable de entorno GEMINI_API_KEY"
                )
        
        super().__init__(api_key, model_name, ia_name=GEMINI_IA_NAME)
        
        # Configuración específica de Gemini
        self.generation_config = {
            'temperature': 0.9,
            'top_p': 1,
            'top_k': 40,
            'max_output_tokens': 20000,
            'stop_sequences': [],
        }
        
        self.safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
        ]
        
        # Inicializar el modelo de Gemini
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=self.generation_config,
            safety_settings=self.safety_settings
        )
    
    def _validate_configuration(self) -> None:
        """
        Valida la configuración del servicio Gemini
        
        Raises:
            ValueError: Si la configuración no es válida
        """
        # Configurar la API key
        if self.api_key:
            genai.configure(api_key=self.api_key)
        else:
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise ValueError(
                    "API key no encontrada. Proporciona una API key o "
                    "configura la variable de entorno GEMINI_API_KEY"
                )
            genai.configure(api_key=api_key)
            self.api_key = api_key
    
    def send_prompt(self, messages: List[IAMessage], is_json:bool, **kwargs) -> IAResponse:
        """
        Envía un prompt a Gemini usando la estructura de mensajes estándar
        
        Args:
            messages: Lista de mensajes IAMessage
            **kwargs: Parámetros adicionales como is_json (bool)
            
        Returns:
            IAResponse: La respuesta de Gemini
            
        Raises:
            ValueError: Si los mensajes no son válidos
            Exception: Si hay un error en la comunicación con Gemini
        """
        # Validar precondiciones (heredadas de la clase base)
        self.validate_messages(messages)
        
        try:
            # Convertir IAMessage a formato de Gemini
            gemini_messages = self._convert_to_gemini_format(messages)
            
            # El último mensaje debe ser del usuario
            if gemini_messages[-1]["role"] != "user":
                raise ValueError("El último mensaje debe ser del usuario")
            
            # Separar historial del último mensaje
            history = gemini_messages[:-1] if len(gemini_messages) > 1 else []
            user_message = gemini_messages[-1]["parts"][0]
            
            # Iniciar chat con historial
            chat = self.model.start_chat(history=history)
            
            # Enviar mensaje
            response = chat.send_message(user_message)
            
            # Procesar respuesta
            if is_json:
                text = response.text.replace("```json", "").replace("```", "")
                try:
                    content = json.loads(text)
                except json.JSONDecodeError:
                    print(f"Error al parsear como JSON: {text}")
                    result = self.send_simple_prompt(f"Ocurrio un error al parsear como JSON: {text} dame el correcto formato sin explicaciones solo el json")
                    try:
                        content = json.loads(result)
                    except json.JSONDecodeError:
                        print(f"Error al parsear como JSON: {result}")
                        result = self.send_simple_prompt(f"Ocurrio por segunda vez un error al parsear como JSON: {text} dame el correcto formato sin explicaciones solo el json")
                        content = json.loads(result)

                        raise Exception(f"Error al parsear como JSON: {result}")
            else:
                content = response.text
            
            # Retornar respuesta en formato estándar (postcondición cumplida)
            return IAResponse(
                content=content,
                model=self.model_name,
                metadata={
                    "service": self.service_name,
                    "is_json": is_json,
                    "safety_ratings": getattr(response, 'safety_ratings', None)
                }
            )
            
        except Exception as e:
            raise Exception(f"Error al comunicarse con Gemini: {str(e)}")
    
    def send_simple_prompt(self, prompt: str, **kwargs) -> str:
        """
        Envía un prompt simple a Gemini
        
        Args:
            prompt: El texto del prompt
            **kwargs: Parámetros adicionales
            
        Returns:
            str: La respuesta de Gemini como texto plano
            
        Raises:
            ValueError: Si el prompt está vacío
            Exception: Si hay un error en la comunicación con Gemini
        """
        # Validar precondiciones (heredadas de la clase base)
        self.validate_prompt(prompt)
        
        # Crear mensaje de usuario y enviar
        messages = [self.create_user_message(prompt)]
        response = self.send_prompt(messages, is_json=False, **kwargs)
        
        # Postcondición: retornar texto no vacío
        if isinstance(response.content, str):
            return response.content
        else:
            return str(response.content)
    
    def _convert_to_gemini_format(self, messages: List[IAMessage]) -> List[Dict[str, Any]]:
        """
        Convierte mensajes IAMessage al formato requerido por Gemini
        
        Args:
            messages: Lista de mensajes IAMessage
            
        Returns:
            Lista de mensajes en formato Gemini
        """
        gemini_messages = []
        
        for message in messages:
            # Mapear roles: system -> user (Gemini no tiene rol system)
            role = message.role
            if role == "system":
                role = "user"
            elif role == "assistant":
                role = "model"
            
            gemini_messages.append({
                "role": role,
                "parts": [message.content]
            })
        
        return gemini_messages
    
    @property
    def service_name(self) -> str:
        """
        Retorna el nombre del servicio
        
        Returns:
            str: "Gemini"
        """
        return "Gemini"
    
    @property
    def default_model(self) -> str:
        """
        Retorna el modelo por defecto de Gemini
        
        Returns:
            str: "gemini-1.5-flash"
        """
        return "gemini-1.5-flash" 