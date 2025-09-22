from modules.content_ia.use_cases.dto import ChatContent
from modules.content_ia.use_cases.summary_use_case.interfaces import IGenerateSummary
from modules.content_ia.use_cases.shared.base_ia import IA, IAMessage

class PremiumGenerateSummary(IGenerateSummary):
    def generate_summary(self, chat_content: ChatContent, ia: IA) -> str:
        prompt = f"""
        Dado el siguiente contenido: {chat_content}
        Genera un resumen de 100 palabras.
        """

        messages = [
            IAMessage(role="user", content=prompt)
        ]

        response = ia.send_prompt(messages, is_json=False)
        return response.content