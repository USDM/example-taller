from modules.content_ia.use_cases.chat_ia_use_case.interfaces.i_send_prompt import ISendPrompt
from modules.content_ia.use_cases.shared.base_ia import IAMessage, IA

class StudentSendPrompt(ISendPrompt):
    def send_prompt(self, comments: list[str], question: str, ia: IA) -> str:
        prompt = f"""
        Dado el siguiente contenido: {comments}
        y la siguiente pregunta: {question}
        Genera una respuesta a la pregunta utilizando un lenguaje informal y coloquial.
        """

        messages = [
            IAMessage(role="user", content=prompt)
        ]

        response = self.ia.send_prompt(messages, is_json=False)
        response_text = response.content 

        return response_text
        
        