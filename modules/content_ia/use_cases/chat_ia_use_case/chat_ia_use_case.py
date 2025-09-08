from modules.content_ia.use_cases.dto import Content
from .interfaces.search_content_repository import SearchContentRepository
from modules.content_ia.use_cases.shared.base_ia import IA, IAMessage

class ChatIAUseCase:

    def __init__(self, search_content_repository: SearchContentRepository, ia: IA):
        self.search_content_repository = search_content_repository
        self.ia = ia

    def chatWithContentIa(self, content_id: int, question: str) -> Content:
        content = self.search_content_repository.get_content(content_id)
        comments = content.comments

        prompt = f"""
        Dado el siguiente contenido: {comments}
        y la siguiente pregunta: {question}
        Genera una respuesta a la pregunta
        """

        messages = [
            IAMessage(role="user", content=prompt)
        ]

        response = self.ia.send_prompt(messages, is_json=False)
        print("acaaa", response)
        pass