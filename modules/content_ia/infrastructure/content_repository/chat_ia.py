from ...use_cases.chat_with_content_use_case.interfaces import ChatIARepository as ChatIARepositoryInterface
from ...use_cases.dto import ContentComment
from ...infrastructure.ia.gemini import GeminiIA
from ...use_cases.shared import IAMessage

class ChatIARepository(ChatIARepositoryInterface):
    def send_prompt(self, question: str, comments: list[ContentComment]) -> str:
        print("enviando prompt a la IA desde la implementacion")        
        prompt = f"""
        Dado el siguiente contenido:
        {comments}
        Responde la pregunta:
        {question}
        """
        response = self._send_prompt(prompt, is_json=False)
        return response

    def _send_prompt(self, prompt:str, is_json:bool) -> str:
        messages = [
            IAMessage(role="user", content=prompt)
        ]
        response = GeminiIA().send_prompt(messages, is_json)
        return response.content