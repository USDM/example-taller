from ..dto import Content
from .interfaces.search_content_by_user_repository import SearchContentByUserRepository
from .interfaces.send_email_repository import SendEmailRepository


class EmailsUseCase:

    def __init__(self, 
        search_content_by_user_repo: SearchContentByUserRepository,
        send_email_repo: SendEmailRepository
    ):
        self.search_content_by_user_repo = search_content_by_user_repo
        self.send_email_repo = send_email_repo

    def send_email(self, user_id: int) -> list[Content]:
        """
            Enviar un correo a un usuario con el contenido asociado

            1.-Recibir el id del usuario
            2.-Obtener los contenidos del usuario
            3.-Enviar correo

            1.- None
            2.-SearchContentByUserRepository
            3.-SendEmailRepository
        """
        contents = self.search_content_by_user_repo.get_content_by_user_id(user_id)
        email = self.search_content_by_user_repo.get_user_email(user_id)
        print(contents, email, "contents")
        self.send_email_repo.send_email(email, contents)
        pass