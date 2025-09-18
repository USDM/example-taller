from modules.content_ia.infrastructure import user_repository
from modules.content_ia.use_cases.dto import Content
from .interfaces.search_content_repository import SearchContentRepository
from .interfaces.i_save_response_ia import ISaveResponseIa
from modules.content_ia.use_cases.shared.base_ia import IA, IAMessage
from .interfaces import (
    FactoryResumeComments,
    FactoryUserComments,
    UserRepository
)
from typing import Optional

class ChatIAUseCase:

    def __init__(self, 
        search_content_repository: Optional[SearchContentRepository] = None, 
        ia: Optional[IA] = None,
        save_response_repo: Optional[ISaveResponseIa] = None,
        factory_resume_comments: Optional[FactoryResumeComments] = None,
        factory_user_comments: Optional[FactoryUserComments] = None,
        search_user_repository: Optional[UserRepository] = None
        ):
        self.search_content_repository = search_content_repository
        self.ia = ia
        self.save_response_repo = save_response_repo
        self.factory_resume_comments = factory_resume_comments
        self.factory_user_comments = factory_user_comments
        self.search_user_repository = search_user_repository

    def chatWithContentIa(self, content_id: int, question: str) -> Content:
        content = self.search_content_repository.get_content(content_id)

        prompt = f"""
        Dado el siguiente contenido: {content}
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

    def generate_resume_comments(self, user_id:int) -> Content:
        """
            1. Obtener el usuario
            2. Obtener los comentarios del chat
            3. Ejecutar prompt para hacer resumen

            1. search_user_repository
            2. factory_user_comments (depende de search_content_repository)
            3. factory_resume_comments (depende de resume_comments_repository)
        """
        user = self.search_user_repository.get_user_type(user_id=user_id)
        user_comments = self.factory_user_comments.create_user_comments(user_type=user)
        comments = user_comments.get_comments(user_id=user_id)
        user_resume = self.factory_resume_comments.create_resume_comments(user_type=user)
        print(user_resume)
        resume = user_resume.resume_ia_prompt(comments=comments)
        print(resume)