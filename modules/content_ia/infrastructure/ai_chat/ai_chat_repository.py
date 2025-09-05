from modules.content_ia.use_cases.dto import Content
from modules.content_ia.use_cases.chat_ia_use_case.interfaces.ai_chat import AIChat
from modules.content_ia.infrastructure.ia.factory_ia import FactoryIA
from modules.content_ia.infrastructure.ia.gemini import GeminiIA

class AiChatRepository(AIChat):

    def __init__(self):
        self.ia = GeminiIA()

    def chat(self, message: str, content: Content) -> str:
        prompt = f"""
        Contenido:
        {content}

        Responde la siguiente pregunta:
        {message}
        """
        response = self.ia.send_simple_prompt(prompt)
        return response