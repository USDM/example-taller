import os
from typing import List, Dict, Any, Optional
import json
from dotenv import load_dotenv

try:
    import anthropic
except ImportError:
    anthropic = None

from ....content_ia.use_cases.shared.base_ia import IA, IAMessage, IAResponse
from modules.content_ia.use_cases.dto import IANames

load_dotenv()

CLAUDE_IA_NAME = "claude"


class ClaudeIA(IA):
    """
    Implementación de Claude que hereda de la clase base IA
    
    Esta clase cumple con el principio LSP (Liskov Substitution Principle):
    - Mantiene las precondiciones y postcondiciones de la clase base
    - Puede sustituir a la clase base sin romper la funcionalidad
    - No fortalece las precondiciones ni debilita las postcondiciones
    """

    def get_ia_name(self) -> str:
        return IANames.CLAUDE.value
    
    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None):
        """
        Inicializa el servicio de Claude
        
        Args:
            api_key: API key de Anthropic Claude (opcional si está en variables de entorno)
            model_name: Nombre del modelo a usar (por defecto claude-3-haiku-20240307)
        """
        if anthropic is None:
            raise ImportError(
                "La librería 'anthropic' no está instalada. "
                "Instálala con: pip install anthropic"
            )
        
        # Establecer el modelo por defecto si no se proporciona
        if model_name is None:
            model_name = self.default_model

        if api_key is None:
            api_key = os.getenv("CLAUDE_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                raise ValueError(
                    "API key no encontrada. Proporciona una API key o "
                    "configura la variable de entorno CLAUDE_API_KEY o ANTHROPIC_API_KEY"
                )
        
        super().__init__(api_key, model_name, ia_name=CLAUDE_IA_NAME)
        
        # Inicializar cliente de Claude
        self.client = anthropic.Anthropic(api_key=self.api_key)
        
        # Configuración por defecto
        self.max_tokens = 8000
        self.temperature = 0.9
    
    def _validate_configuration(self) -> None:
        """
        Valida la configuración del servicio Claude
        
        Raises:
            ValueError: Si la configuración no es válida
        """
        # Obtener API key
        if not self.api_key:
            api_key = os.getenv("CLAUDE_API_KEY") or os.getenv("ANTHROPIC_API_KEY")
            if not api_key:
                raise ValueError(
                    "API key no encontrada. Proporciona una API key o "
                    "configura la variable de entorno CLAUDE_API_KEY o ANTHROPIC_API_KEY"
                )
            self.api_key = api_key
    
    def send_prompt(self, messages: List[IAMessage], is_json:bool, **kwargs) -> IAResponse:
        """
        Envía un prompt a Claude usando la estructura de mensajes estándar
        
        Args:
            messages: Lista de mensajes IAMessage
            **kwargs: Parámetros adicionales como max_tokens (int), temperature (float)
            
        Returns:
            IAResponse: La respuesta de Claude
            
        Raises:
            ValueError: Si los mensajes no son válidos
            Exception: Si hay un error en la comunicación con Claude
        """
        # Validar precondiciones (heredadas de la clase base)
        self.validate_messages(messages)
        
        try:
            # Convertir IAMessage a formato de Claude
            claude_messages, system_message = self._convert_to_claude_format(messages)
            
            # Configurar parámetros
            max_tokens = kwargs.get('max_tokens', self.max_tokens)
            temperature = kwargs.get('temperature', self.temperature)
            
            # Preparar argumentos para la API
            api_args = {
                'model': self.model_name,
                'max_tokens': max_tokens,
                'temperature': temperature,
                'messages': claude_messages
            }
            
            # Agregar mensaje de sistema si existe
            if system_message:
                api_args['system'] = system_message
            
            # Enviar mensaje
            response = self.client.messages.create(**api_args)
            
            # Extraer contenido de la respuesta
            content = ""
            if response.content and len(response.content) > 0:
                content = response.content[0].text
            
            # Procesar como JSON si se solicita
            if is_json and content:
                cleaned_content = content.replace("```json", "").replace("```", "").strip()
                try:
                    content = json.loads(cleaned_content)
                except json.JSONDecodeError:
                    print(f"Error al parsear como JSON: {cleaned_content}")
                    result = self.send_simple_prompt(f"Ocurrio un error al parsear como JSON: {cleaned_content} dame el correcto formato sin explicaciones solo el json")
                    content = json.loads(result)
                  
            
            # Retornar respuesta en formato estándar (postcondición cumplida)
            return IAResponse(
                content=content,
                model=self.model_name,
                tokens_used=response.usage.output_tokens if hasattr(response, 'usage') else None,
                metadata={
                    "service": self.service_name,
                    "is_json": is_json,
                    "input_tokens": response.usage.input_tokens if hasattr(response, 'usage') else None,
                    "stop_reason": response.stop_reason if hasattr(response, 'stop_reason') else None
                }
            )
            
        except Exception as e:
            raise Exception(f"Error al comunicarse con Claude: {str(e)}")
    
    def send_simple_prompt(self, prompt: str, **kwargs) -> str:
        """
        Envía un prompt simple a Claude
        
        Args:
            prompt: El texto del prompt
            **kwargs: Parámetros adicionales
            
        Returns:
            str: La respuesta de Claude como texto plano
            
        Raises:
            ValueError: Si el prompt está vacío
            Exception: Si hay un error en la comunicación con Claude
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
    
    def _convert_to_claude_format(self, messages: List[IAMessage]) -> tuple[List[Dict[str, str]], Optional[str]]:
        """
        Convierte mensajes IAMessage al formato requerido por Claude
        
        Args:
            messages: Lista de mensajes IAMessage
            
        Returns:
            Tupla con (lista de mensajes para Claude, mensaje de sistema)
        """
        claude_messages = []
        system_message = None
        
        for message in messages:
            if message.role == "system":
                # Claude maneja los mensajes de sistema por separado
                if system_message is None:
                    system_message = message.content
                else:
                    # Si hay múltiples mensajes de sistema, concatenarlos
                    system_message += "\n\n" + message.content
            else:
                # Mapear roles: assistant se mantiene igual, user se mantiene igual
                role = message.role
                if role == "assistant":
                    role = "assistant"
                elif role == "user":
                    role = "user"
                
                claude_messages.append({
                    "role": role,
                    "content": message.content
                })
        
        return claude_messages, system_message
    
    @property
    def service_name(self) -> str:
        """
        Retorna el nombre del servicio
        
        Returns:
            str: "Claude"
        """
        return "Claude"
    
    @property
    def default_model(self) -> str:
        """
        Retorna el modelo por defecto de Claude
        
        Returns:
            str: "claude-3-haiku-20240307"
        """
        return "claude-sonnet-4-20250514" 