from modules.content_ia.use_cases.dto import Content
from .interfaces.search_content import SearchContent
from .interfaces.ai_chat import AIChat

class ChatIAUseCase:

    def __init__(self, search_content: SearchContent, ai_chat: AIChat):
        self.search_content = search_content
        self.ai_chat = ai_chat

    def chat_ia(self, message: str, content_id: int) -> str:
        """
        1. Recibir un mensaje del usuario y el id del contenido
        2. Obtener contenido del id
        3. Enviar mensaje al IA
        4. Retornar respuesta del IA

        1. -
        2. content_repository.get_content(content_id)
        3. ia.send_prompt(message, content)
        4. -
        """

        content = self.search_content.search(content_id)
        response = self.ai_chat.chat(message, content)
        return response


