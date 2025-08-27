import os
import google.generativeai as genai
from typing import List, Dict, Any, Optional
import json
from dotenv import load_dotenv
import base64
import mimetypes
import io

try:
    from PIL import Image
except ImportError:
    Image = None

from modules.content_ia.use_cases.shared import IA, IAMessage, IAResponse, IAFile
from modules.content_ia.use_cases.dto import IANames

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
    
    def _upload_file_to_gemini(self, file: IAFile) -> Any:
        """
        Sube un archivo a Gemini File API
        
        Args:
            file: Archivo a subir
            
        Returns:
            Objeto de archivo de Gemini
        """
        if file.path and os.path.exists(file.path):
            # Subir archivo desde ruta
            uploaded_file = genai.upload_file(
                path=file.path,
                mime_type=file.mime_type,
                display_name=file.name
            )
        elif file.data:
            # Para datos en base64, necesitamos crear un archivo temporal
            import tempfile
            
            # Decodificar base64
            file_data = base64.b64decode(file.data)
            
            # Crear archivo temporal
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file.name.split('.')[-1] if file.name else 'tmp'}") as temp_file:
                temp_file.write(file_data)
                temp_path = temp_file.name
            
            try:
                uploaded_file = genai.upload_file(
                    path=temp_path,
                    mime_type=file.mime_type,
                    display_name=file.name or "uploaded_file"
                )
            finally:
                # Limpiar archivo temporal
                os.unlink(temp_path)
        else:
            raise ValueError("El archivo debe tener una ruta válida o datos en base64")
        
        return uploaded_file
    
    def _upload_image_to_gemini(self, image_file: IAFile) -> Any:
        """
        Sube una imagen específicamente a Gemini con validaciones adicionales
        
        Args:
            image_file: Archivo de imagen a subir
            
        Returns:
            Objeto de archivo de Gemini para la imagen
            
        Raises:
            ValueError: Si la imagen no es válida o no está soportada
        """
        # Validar que es una imagen
        if not self.validate_image_file(image_file):
            raise ValueError(f"El archivo {image_file.name} no es una imagen válida")
        
        # Formatos soportados por Gemini
        supported_formats = ['image/jpeg', 'image/png', 'image/gif', 'image/webp']
        if image_file.mime_type not in supported_formats:
            raise ValueError(f"El formato {image_file.mime_type} no está soportado por Gemini. Formatos soportados: {supported_formats}")
        
        # Validar tamaño de imagen si es posible
        if image_file.path and os.path.exists(image_file.path):
            try:
                # Validar tamaño de archivo
                max_size = 20 * 1024 * 1024  # 20MB
                file_size = os.path.getsize(image_file.path)
                if file_size > max_size:
                    raise ValueError(f"La imagen es demasiado grande ({file_size} bytes). Tamaño máximo: {max_size} bytes")
                
                # Validar dimensiones si PIL está disponible
                if Image is not None:
                    with Image.open(image_file.path) as img:
                        # Validar dimensiones (Gemini soporta hasta 3072x3072)
                        max_dimension = 3072
                        if img.width > max_dimension or img.height > max_dimension:
                            print(f"Advertencia: La imagen {img.width}x{img.height} puede ser redimensionada por Gemini (máximo recomendado: {max_dimension}x{max_dimension})")
                else:
                    print("Advertencia: PIL no está disponible, no se pueden validar las dimensiones de la imagen")
            except Exception as e:
                print(f"Advertencia: No se pudo validar la imagen {image_file.name}: {str(e)}")
        
        # Usar el método base para subir el archivo
        return self._upload_file_to_gemini(image_file)
    
    def send_prompt_with_images(self, messages: List[IAMessage], is_json: bool = False, **kwargs) -> IAResponse:
        """
        Envía un prompt a Gemini con imágenes adjuntas
        Optimizado específicamente para el manejo de imágenes
        
        Args:
            messages: Lista de mensajes IAMessage que pueden contener imágenes
            is_json: Si la respuesta debe ser JSON
            **kwargs: Parámetros adicionales
            
        Returns:
            IAResponse: La respuesta de Gemini
            
        Raises:
            ValueError: Si las imágenes no son válidas
        """
        # Validar precondiciones
        self.validate_messages(messages)
        
        # Validar específicamente las imágenes
        for message in messages:
            if message.files:
                for file in message.files:
                    if not self.validate_image_file(file):
                        raise ValueError(f"El archivo {file.name} no es una imagen válida")
        
        try:
            # Subir imágenes a Gemini con validaciones específicas
            uploaded_files = []
            for message in messages:
                if message.files:
                    for file in message.files:
                        if self.validate_image_file(file):
                            uploaded_file = self._upload_image_to_gemini(file)
                            uploaded_files.append(uploaded_file)
                        else:
                            # Si no es imagen, usar el método general
                            uploaded_file = self._upload_file_to_gemini(file)
                            uploaded_files.append(uploaded_file)
            
            # Convertir mensajes al formato de Gemini
            gemini_messages = self._convert_to_gemini_format_with_files(messages, uploaded_files)
            
            # El último mensaje debe ser del usuario
            if gemini_messages[-1]["role"] != "user":
                raise ValueError("El último mensaje debe ser del usuario")
            
            # Separar historial del último mensaje
            history = gemini_messages[:-1] if len(gemini_messages) > 1 else []
            user_message_parts = gemini_messages[-1]["parts"]
            
            # Iniciar chat con historial
            chat = self.model.start_chat(history=history)
            
            # Enviar mensaje con imágenes
            response = chat.send_message(user_message_parts)
            
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
            
            # Retornar respuesta en formato estándar
            return IAResponse(
                content=content,
                model=self.model_name,
                metadata={
                    "service": self.service_name,
                    "is_json": is_json,
                    "images_uploaded": len([f for f in uploaded_files if any(self.validate_image_file(file) for message in messages if message.files for file in message.files)]),
                    "total_files_uploaded": len(uploaded_files),
                    "safety_ratings": getattr(response, 'safety_ratings', None)
                }
            )
            
        except Exception as e:
            raise Exception(f"Error al comunicarse con Gemini: {str(e)}")
    
    def send_simple_prompt_with_image(self, prompt: str, image_path: str, **kwargs) -> str:
        """
        Envía un prompt simple con una imagen a Gemini
        
        Args:
            prompt: El texto del prompt
            image_path: Ruta a la imagen
            **kwargs: Parámetros adicionales
            
        Returns:
            str: La respuesta de Gemini como texto plano
        """
        # Crear mensaje con imagen
        message = self.create_user_message_with_image(prompt, image_path)
        response = self.send_prompt_with_images([message], is_json=False, **kwargs)
        
        if isinstance(response.content, str):
            return response.content
        else:
            return str(response.content)
    
    def send_simple_prompt_with_images(self, prompt: str, image_paths: List[str], **kwargs) -> str:
        """
        Envía un prompt simple con múltiples imágenes a Gemini
        
        Args:
            prompt: El texto del prompt
            image_paths: Lista de rutas a las imágenes
            **kwargs: Parámetros adicionales
            
        Returns:
            str: La respuesta de Gemini como texto plano
        """
        # Crear mensaje con múltiples imágenes
        message = self.create_user_message_with_images(prompt, image_paths)
        response = self.send_prompt_with_images([message], is_json=False, **kwargs)
        
        if isinstance(response.content, str):
            return response.content
        else:
            return str(response.content)
    
    def analyze_image(self, image_path: str, analysis_prompt: str = "Describe esta imagen en detalle", **kwargs) -> str:
        """
        Analiza una imagen con un prompt específico
        
        Args:
            image_path: Ruta a la imagen
            analysis_prompt: Prompt para el análisis (por defecto describe la imagen)
            **kwargs: Parámetros adicionales
            
        Returns:
            str: Análisis de la imagen
        """
        return self.send_simple_prompt_with_image(analysis_prompt, image_path, **kwargs)
    
    def compare_images(self, image_paths: List[str], comparison_prompt: str = "Compara estas imágenes y describe las diferencias y similitudes", **kwargs) -> str:
        """
        Compara múltiples imágenes
        
        Args:
            image_paths: Lista de rutas a las imágenes a comparar
            comparison_prompt: Prompt para la comparación
            **kwargs: Parámetros adicionales
            
        Returns:
            str: Comparación de las imágenes
        """
        if len(image_paths) < 2:
            raise ValueError("Se necesitan al menos 2 imágenes para comparar")
        
        return self.send_simple_prompt_with_images(comparison_prompt, image_paths, **kwargs)
    
    def send_prompt_with_files(self, messages: List[IAMessage], is_json: bool = False, **kwargs) -> IAResponse:
        """
        Envía un prompt a Gemini con archivos adjuntos
        
        Args:
            messages: Lista de mensajes IAMessage (puede incluir archivos)
            is_json: Si la respuesta debe ser JSON
            **kwargs: Parámetros adicionales
            
        Returns:
            IAResponse: La respuesta de Gemini
        """
        # Validar precondiciones
        self.validate_messages(messages)
        
        try:
            # Subir archivos a Gemini
            uploaded_files = []
            for message in messages:
                if message.files:
                    for file in message.files:
                        uploaded_file = self._upload_file_to_gemini(file)
                        uploaded_files.append(uploaded_file)
            
            # Convertir mensajes al formato de Gemini
            gemini_messages = self._convert_to_gemini_format_with_files(messages, uploaded_files)
            
            # El último mensaje debe ser del usuario
            if gemini_messages[-1]["role"] != "user":
                raise ValueError("El último mensaje debe ser del usuario")
            
            # Separar historial del último mensaje
            history = gemini_messages[:-1] if len(gemini_messages) > 1 else []
            user_message_parts = gemini_messages[-1]["parts"]
            
            # Iniciar chat con historial
            chat = self.model.start_chat(history=history)
            
            # Enviar mensaje con archivos
            response = chat.send_message(user_message_parts)
            
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
                        try:
                            content = json.loads(result)
                        except json.JSONDecodeError:
                            raise Exception(f"Error al parsear como JSON después de múltiples intentos: {result}")
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
    
    def _convert_to_gemini_format_with_files(self, messages: List[IAMessage], uploaded_files: List[Any]) -> List[Dict[str, Any]]:
        """
        Convierte mensajes con archivos al formato de Gemini
        
        Args:
            messages: Lista de mensajes IAMessage
            uploaded_files: Lista de archivos subidos a Gemini
            
        Returns:
            Lista de mensajes en formato Gemini con archivos
        """
        gemini_messages = []
        file_index = 0
        
        for message in messages:
            # Mapear roles
            role = message.role
            if role == "system":
                role = "user"
            elif role == "assistant":
                role = "model"
            
            # Crear partes del mensaje
            parts = [message.content]
            
            # Agregar archivos si los hay
            if message.files:
                for file in message.files:
                    if file_index < len(uploaded_files):
                        parts.append(uploaded_files[file_index])
                        file_index += 1
            
            gemini_messages.append({
                "role": role,
                "parts": parts
            })
        
        return gemini_messages
    
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