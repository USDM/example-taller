from .base_ia import IA, IAMessage, IAResponse
from typing import List, Optional

class ChatGPT(IA):
    """
    Clase base abstracta para servicios de IA
    
    Esta clase define la interfaz común que deben implementar todos los servicios de IA,
    garantizando que puedan ser intercambiables (principio LSP de SOLID).
    
    Todas las subclases deben:
    1. Implementar los métodos abstractos
    2. Mantener las precondiciones y postcondiciones de la clase base
    3. No fortalecer las precondiciones ni debilitar las postcondiciones
    """
    
    def __init__(self, api_key: Optional[str] = None, model_name: Optional[str] = None, ia_name: Optional[str] = None):
        """
        Inicializa el servicio de IA
        
        Args:
            api_key: Clave de API del servicio (opcional si está en variables de entorno)
            model_name: Nombre del modelo a utilizar (opcional, usará el por defecto)
        """
        self.api_key = api_key
        self.model_name = model_name
        self.ia_name = ia_name
        self._validate_configuration()

    
    def get_ia_name(self) -> str:
        """
        Retorna el nombre del servicio de IA
        """
        pass
    
    
    def _validate_configuration(self) -> None:
        """
        Valida la configuración del servicio
        
        Raises:
            ValueError: Si la configuración no es válida
        """
        pass
    
    
    def send_prompt(self, messages: List[IAMessage], **kwargs) -> IAResponse:
        """
        Envía un prompt al servicio de IA
        
        Args:
            messages: Lista de mensajes para enviar
            **kwargs: Parámetros adicionales específicos del servicio
            
        Returns:
            IAResponse: La respuesta del servicio de IA
            
        Raises:
            ValueError: Si los mensajes no son válidos
            Exception: Si hay un error en la comunicación con el servicio
            
        Precondiciones:
        - messages no debe estar vacío
        - Cada mensaje debe tener un role válido ("user", "assistant", "system")
        - Cada mensaje debe tener contenido no vacío
        
        Postcondiciones:
        - Retorna una respuesta válida con contenido
        - La respuesta contiene información del modelo utilizado
        """
        pass
    
    
    def send_simple_prompt(self, prompt: str, **kwargs) -> str:
        """
        Envía un prompt simple al servicio de IA
        
        Args:
            prompt: El texto del prompt
            **kwargs: Parámetros adicionales específicos del servicio
            
        Returns:
            str: La respuesta del servicio como texto plano
            
        Raises:
            ValueError: Si el prompt está vacío
            Exception: Si hay un error en la comunicación con el servicio
            
        Precondiciones:
        - prompt no debe estar vacío o ser None
        
        Postcondiciones:
        - Retorna una cadena de texto no vacía
        """
        pass
    
    def validate_messages(self, messages: List[IAMessage]) -> None:
        """
        Valida que la lista de mensajes sea correcta
        
        Args:
            messages: Lista de mensajes a validar
            
        Raises:
            ValueError: Si la estructura no es válida
        """
        if not messages:
            raise ValueError("La lista de mensajes no puede estar vacía")
        
        valid_roles = {"user", "assistant", "system"}
        
        for i, message in enumerate(messages):
            if not isinstance(message, IAMessage):
                raise ValueError(f"El mensaje {i} debe ser una instancia de IAMessage")
            
            if message.role not in valid_roles:
                raise ValueError(f"El rol del mensaje {i} debe ser uno de: {valid_roles}")
            
            if not message.content or not message.content.strip():
                raise ValueError(f"El contenido del mensaje {i} no puede estar vacío")
    
    def validate_prompt(self, prompt: str) -> None:
        """
        Valida que el prompt sea correcto
        
        Args:
            prompt: El prompt a validar
            
        Raises:
            ValueError: Si el prompt no es válido
        """
        if not prompt or not prompt.strip():
            raise ValueError("El prompt no puede estar vacío")
    
    def create_user_message(self, content: str) -> IAMessage:
        """
        Crea un mensaje de usuario
        
        Args:
            content: El contenido del mensaje
            
        Returns:
            IAMessage: Mensaje con rol de usuario
        """
        return IAMessage(role="user", content=content)
    
    def create_assistant_message(self, content: str) -> IAMessage:
        """
        Crea un mensaje del asistente
        
        Args:
            content: El contenido del mensaje
            
        Returns:
            IAMessage: Mensaje con rol de asistente
        """
        return IAMessage(role="assistant", content=content)
    
    def create_system_message(self, content: str) -> IAMessage:
        """
        Crea un mensaje del sistema
        
        Args:
            content: El contenido del mensaje
            
        Returns:
            IAMessage: Mensaje con rol de sistema
        """
        return IAMessage(role="system", content=content)
    
    @property
    
    def service_name(self) -> str:
        """
        Retorna el nombre del servicio de IA
        
        Returns:
            str: Nombre del servicio
        """
        pass
    
    @property
    
    def default_model(self) -> str:
        """
        Retorna el modelo por defecto del servicio
        
        Returns:
            str: Nombre del modelo por defecto
        """
        pass 