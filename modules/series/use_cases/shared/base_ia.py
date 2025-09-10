from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import os
import mimetypes

@dataclass
class IAFile:
    """
    Estructura para representar archivos adjuntos en mensajes de IA
    
    Args:
        path: Ruta al archivo
        mime_type: Tipo MIME del archivo
        name: Nombre del archivo (opcional)
        data: Datos del archivo en base64 (opcional, para archivos en memoria)
    """
    path: Optional[str] = None
    mime_type: str = "application/octet-stream"
    name: Optional[str] = None
    data: Optional[str] = None


@dataclass
class IAMessage:
    """
    Estructura estándar para los mensajes de IA
    
    Args:
        role: El rol del mensaje ("user", "assistant", "system")
        content: El contenido del mensaje
        files: Lista de archivos adjuntos (opcional)
        metadata: Información adicional opcional
    """
    role: str
    content: str
    files: Optional[List[IAFile]] = None
    metadata: Optional[Dict[str, Any]] = None


@dataclass
class IAResponse:
    """
    Estructura estándar para las respuestas de IA
    
    Args:
        content: El contenido de la respuesta
        model: El modelo que generó la respuesta
        tokens_used: Cantidad de tokens utilizados (opcional)
        metadata: Información adicional opcional
    """
    content: str|dict
    model: str
    tokens_used: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = None


class IA(ABC):
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

    @abstractmethod
    def get_ia_name(self) -> str:
        """
        Retorna el nombre del servicio de IA
        """
        pass
    
    @abstractmethod
    def _validate_configuration(self) -> None:
        """
        Valida la configuración del servicio
        
        Raises:
            ValueError: Si la configuración no es válida
        """
        pass
    
    @abstractmethod
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
    
    @abstractmethod
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
    
    def create_user_message_with_files(self, content: str, files: List[IAFile]) -> IAMessage:
        """
        Crea un mensaje de usuario con archivos adjuntos
        
        Args:
            content: El contenido del mensaje
            files: Lista de archivos adjuntos
            
        Returns:
            IAMessage: Mensaje con rol de usuario y archivos
        """
        return IAMessage(role="user", content=content, files=files)
    
    def create_file_from_path(self, file_path: str, mime_type: str = None, name: str = None) -> IAFile:
        """
        Crea un IAFile desde una ruta de archivo
        
        Args:
            file_path: Ruta al archivo
            mime_type: Tipo MIME del archivo (se detecta automáticamente si no se proporciona)
            name: Nombre del archivo (se usa el nombre del archivo si no se proporciona)
            
        Returns:
            IAFile: Archivo configurado
        """
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"El archivo {file_path} no existe")
        
        if mime_type is None:
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type is None:
                mime_type = "application/octet-stream"
        
        if name is None:
            name = os.path.basename(file_path)
        
        return IAFile(path=file_path, mime_type=mime_type, name=name)
    
    def create_image_from_path(self, image_path: str, name: str = None) -> IAFile:
        """
        Crea un IAFile específico para imágenes desde una ruta
        
        Args:
            image_path: Ruta a la imagen
            name: Nombre personalizado para la imagen (opcional)
            
        Returns:
            IAFile: Archivo de imagen configurado
            
        Raises:
            FileNotFoundError: Si la imagen no existe
            ValueError: Si el archivo no es una imagen válida
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"La imagen {image_path} no existe")
        
        # Detectar tipo MIME
        mime_type, _ = mimetypes.guess_type(image_path)
        
        # Validar que es una imagen
        if not mime_type or not mime_type.startswith('image/'):
            raise ValueError(f"El archivo {image_path} no es una imagen válida")
        
        # Validar formatos de imagen soportados comúnmente
        supported_formats = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/webp', 'image/bmp']
        if mime_type not in supported_formats:
            print(f"Advertencia: El formato {mime_type} puede no ser soportado por todos los servicios de IA")
        
        if name is None:
            name = os.path.basename(image_path)
        
        return IAFile(path=image_path, mime_type=mime_type, name=name)
    
    def create_image_from_base64(self, base64_data: str, mime_type: str = "image/jpeg", name: str = "image") -> IAFile:
        """
        Crea un IAFile para imágenes desde datos en base64
        
        Args:
            base64_data: Datos de la imagen en formato base64
            mime_type: Tipo MIME de la imagen (por defecto image/jpeg)
            name: Nombre de la imagen (por defecto "image")
            
        Returns:
            IAFile: Archivo de imagen configurado
            
        Raises:
            ValueError: Si los datos base64 no son válidos o el tipo MIME no es de imagen
        """
        if not mime_type.startswith('image/'):
            raise ValueError(f"El tipo MIME {mime_type} no es válido para imágenes")
        
        if not base64_data:
            raise ValueError("Los datos base64 no pueden estar vacíos")
        
        # Validar que es base64 válido
        try:
            import base64
            base64.b64decode(base64_data, validate=True)
        except Exception as e:
            raise ValueError(f"Los datos base64 no son válidos: {str(e)}")
        
        return IAFile(data=base64_data, mime_type=mime_type, name=name)
    
    def create_user_message_with_image(self, content: str, image_path: str) -> IAMessage:
        """
        Crea un mensaje de usuario con una imagen adjunta
        
        Args:
            content: El contenido del mensaje
            image_path: Ruta a la imagen
            
        Returns:
            IAMessage: Mensaje con rol de usuario e imagen adjunta
        """
        image_file = self.create_image_from_path(image_path)
        return IAMessage(role="user", content=content, files=[image_file])
    
    def create_user_message_with_images(self, content: str, image_paths: List[str]) -> IAMessage:
        """
        Crea un mensaje de usuario con múltiples imágenes adjuntas
        
        Args:
            content: El contenido del mensaje
            image_paths: Lista de rutas a las imágenes
            
        Returns:
            IAMessage: Mensaje con rol de usuario e imágenes adjuntas
        """
        image_files = [self.create_image_from_path(path) for path in image_paths]
        return IAMessage(role="user", content=content, files=image_files)
    
    def validate_image_file(self, file: IAFile) -> bool:
        """
        Valida que un archivo sea una imagen válida
        
        Args:
            file: Archivo a validar
            
        Returns:
            bool: True si es una imagen válida, False en caso contrario
        """
        if not file.mime_type:
            return False
        
        return file.mime_type.startswith('image/')
    
    def send_prompt_with_images(self, messages: List[IAMessage], **kwargs) -> IAResponse:
        """
        Método base para enviar prompts con imágenes
        Por defecto, delega al método send_prompt_with_files si existe,
        o al método send_prompt estándar
        
        Args:
            messages: Lista de mensajes que pueden contener imágenes
            **kwargs: Parámetros adicionales
            
        Returns:
            IAResponse: La respuesta del servicio de IA
        """
        # Validar que las imágenes en los mensajes sean válidas
        for message in messages:
            if message.files:
                for file in message.files:
                    if not self.validate_image_file(file):
                        raise ValueError(f"El archivo {file.name} no es una imagen válida")
        
        # Si la subclase tiene send_prompt_with_files, usarlo
        if hasattr(self, 'send_prompt_with_files') and callable(getattr(self, 'send_prompt_with_files')):
            return self.send_prompt_with_files(messages, **kwargs)
        else:
            # Fallback al método estándar (las subclases deben sobrescribir este método si soportan imágenes)
            print("Advertencia: Este servicio de IA no soporta imágenes de forma nativa")
            return self.send_prompt(messages, **kwargs)
    
    @property
    @abstractmethod
    def service_name(self) -> str:
        """
        Retorna el nombre del servicio de IA
        
        Returns:
            str: Nombre del servicio
        """
        pass
    
    @property
    @abstractmethod
    def default_model(self) -> str:
        """
        Retorna el modelo por defecto del servicio
        
        Returns:
            str: Nombre del modelo por defecto
        """
        pass 