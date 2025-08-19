import os
import google.generativeai as genai
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from dotenv import load_dotenv
import json
load_dotenv()

@dataclass
class GeminiMessage:
    """
    Estructura para los mensajes de Gemini
    
    Args:
        role: El rol del mensaje ("user" o "model")
        parts: Lista de contenido del mensaje (puede ser texto o archivos)
    """
    role: str
    parts: List[str]
    
    def __init__(self, role: str, content: str):
        """
        Inicializa un nuevo mensaje de Gemini
        
        Args:
            role (str): El rol del emisor ("user" o "model")
            content (str): El contenido del mensaje
        """
        self.role = role
        self.parts = [content]


class GeminiService:
    """
    Servicio para interactuar con la API de Gemini
    
    Esta clase maneja la configuración y comunicación con la API de Gemini,
    permitiendo enviar mensajes con la estructura correcta que requiere la API.
    """
    
    def __init__(self, api_key: Optional[str] = None, model_name: str = "gemini-1.5-flash"):
        """
        Inicializa el servicio de Gemini
        
        Args:
            api_key: API key de Google Gemini. Si no se proporciona, se busca en la variable de entorno GEMINI_API_KEY
            model_name: Nombre del modelo a usar (por defecto gemini-pro)
        """
        # Configurar la API key
        if api_key:
            genai.configure(api_key=api_key)
        else:
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("API key no encontrada. Proporciona una API key o configura la variable de entorno GEMINI_API_KEY")
            genai.configure(api_key=api_key)
        
        # Configuración de generación
        self.generation_config = {
            'temperature': 0.9,
            'top_p': 1,
            'top_k': 40,
            'max_output_tokens': 2048,
            'stop_sequences': [],
        }
        
        # Configuración de seguridad
        self.safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
        ]
        
        # Inicializar el modelo
        self.model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=self.generation_config,
            safety_settings=self.safety_settings
        )
    
    def send_prompt(self, messages: List[Dict[str, Any]], is_json: bool) -> str|dict:
        """
        Envía un prompt a Gemini usando la estructura de mensajes correcta
        
        Args:
            messages: Lista de mensajes con la estructura que requiere Gemini.
                     Cada mensaje debe tener:
                     - role: "user" o "model"
                     - parts: lista de strings con el contenido
                     
                     Ejemplo:
                     [
                         {"role": "user", "parts": ["Hola, ¿cómo estás?"]},
                         {"role": "model", "parts": ["¡Hola! Estoy bien, gracias por preguntar."]},
                         {"role": "user", "parts": ["¿Puedes ayudarme con algo?"]}
                     ]
        
        Returns:
            str: La respuesta generada por Gemini
            
        Raises:
            ValueError: Si la estructura de mensajes no es válida
            Exception: Si hay un error en la comunicación con la API
        """
        try:
            # Validar estructura de mensajes
            self._validate_messages(messages)
            
            # Preparar el historial de conversación
            # El último mensaje debe ser del usuario para generar una respuesta
            if not messages:
                raise ValueError("La lista de mensajes no puede estar vacía")
            
            last_message = messages[-1]
            if last_message["role"] != "user":
                raise ValueError("El último mensaje debe ser del usuario")
            
            # Separar el historial del último mensaje
            history = messages[:-1] if len(messages) > 1 else []
            user_message = last_message["parts"][0]
            
            # Iniciar el chat con historial
            chat = self.model.start_chat(history=history)
            
            # Enviar el mensaje del usuario
            response = chat.send_message(user_message)

            if is_json:
                text = response.text.replace("```json", "").replace("```", "")
                print("@TEXT",text)
                return json.loads(text)
            else:
                return response.text
            
        except Exception as e:
            raise Exception(f"Error al comunicarse con Gemini: {str(e)}")
    
    def _validate_messages(self, messages: List[Dict[str, Any]]) -> None:
        """
        Valida que la estructura de mensajes sea correcta
        
        Args:
            messages: Lista de mensajes a validar
            
        Raises:
            ValueError: Si la estructura no es válida
        """
        if not isinstance(messages, list):
            raise ValueError("Los mensajes deben ser una lista")
        
        for i, message in enumerate(messages):
            if not isinstance(message, dict):
                raise ValueError(f"El mensaje {i} debe ser un diccionario")
            
            if "role" not in message:
                raise ValueError(f"El mensaje {i} debe tener un campo 'role'")
            
            if "parts" not in message:
                raise ValueError(f"El mensaje {i} debe tener un campo 'parts'")
            
            if message["role"] not in ["user", "model"]:
                raise ValueError(f"El rol del mensaje {i} debe ser 'user' o 'model'")
            
            if not isinstance(message["parts"], list):
                raise ValueError(f"El campo 'parts' del mensaje {i} debe ser una lista")
            
            if not message["parts"]:
                raise ValueError(f"El campo 'parts' del mensaje {i} no puede estar vacío")
    
    def create_simple_prompt(self, prompt: str) -> List[Dict[str, Any]]:
        """
        Crea una estructura de mensaje simple para un prompt único
        
        Args:
            prompt: El texto del prompt
            
        Returns:
            Lista con un solo mensaje de usuario
        """
        return [{"role": "user", "parts": [prompt]}]
    


# Ejemplo de uso
"""
if __name__ == "__main__":
    # Ejemplo básico
    ejemplo_messages = [
        {"role": "user", "parts": ["Hola, ¿puedes ayudarme a escribir un email profesional?"]},
        {"role": "model", "parts": ["¡Por supuesto! Estaré encantado de ayudarte a escribir un email profesional. ¿Podrías contarme más detalles sobre el propósito del email?"]},
        {"role": "user", "parts": ["Necesito escribir un email para solicitar una reunión con mi jefe"]}
    ]
    
    try:
        service = GeminiService()
        respuesta = service.send_prompt(ejemplo_messages)
        print("Respuesta de Gemini:")
        print(respuesta)
    except Exception as e:
        print(f"Error: {e}")

"""