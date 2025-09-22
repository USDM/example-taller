from modules.content_ia.use_cases.chat_ia_use_case.interfaces.i_send_prompt import ISendPrompt
from modules.content_ia.use_cases.shared.base_ia import IAMessage, IA

class SuscribedSendPrompt(ISendPrompt):
    def send_prompt(self, comments: list[str], question: str, ia: IA) -> str:
        prompt = f"""
        Dado el siguiente contenido: {comments}
        y la siguiente pregunta: {question}
        Genera una respuesta a la pregunta utilizando un lenguaje formal y profesional.
        """

        messages = [
            IAMessage(role="user", content=prompt)
        ]

        response = ia.send_prompt(messages, is_json=False)
        response_text = response.content 

        print(response_text, "response_text desde suscribed")
        return response_text
        
        