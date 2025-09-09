from modules.content_ia.use_cases.dto import Content
from .interfaces.search_content_repository import SearchContentRepository
from .interfaces.i_save_response_ia import ISaveResponseIa
from modules.content_ia.use_cases.shared.base_ia import IA, IAMessage

class ChatIAUseCase:

    def __init__(self, 
        search_content_repository: SearchContentRepository, 
        ia: IA,
        save_response_repo: ISaveResponseIa
        ):
        self.search_content_repository = search_content_repository
        self.ia = ia
        self.save_response_repo = save_response_repo

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
        response_text = response.content 

        self.save_response_repo.save_response(response_text)

        pass