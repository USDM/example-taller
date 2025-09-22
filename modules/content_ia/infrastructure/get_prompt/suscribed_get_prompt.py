from ...use_cases.chat_ia_use_case.interfaces import GetPromptInterface

class SuscribedGetPrompt(GetPromptInterface):
    def get_prompt(self, comments: list[str], question: str) -> str:
        prompt = f"""
        Dado el siguiente contenido: {comments}
        y la siguiente pregunta: {question}
        Genera una respuesta a la pregunta
        """
        return prompt