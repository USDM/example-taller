from ...use_cases.chat_ia_use_case.interfaces import ResumeCommentsRepository
from modules.content_ia.use_cases.shared.base_ia import IAMessage
from ..ia import GeminiIA

class ResumeCommentRepository(ResumeCommentsRepository):
    def resume_ia_prompt(self, comments:list) -> str:
        prompt= f"""
            Dado los siguientes comentarios, generame un resumen detallado con una opnión constructiva
            regresame tu respuesta en html.
            Comentarios: {comments}
        """

        messages = [
            IAMessage(role="user", content=prompt)
        ]

        response = GeminiIA().send_prompt(messages, is_json=False)
        return response.content 