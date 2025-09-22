import os
from modules.content_ia.use_cases.dto import Content
from .interfaces.search_content_repository import SearchContentRepository
from .interfaces.i_save_response_ia import ISaveResponseIa
from modules.content_ia.use_cases.shared.base_ia import IA, IAMessage
from ...use_cases.generate_content_use_case.interfaces import FactoryUserRepository
from .interfaces.i_send_message import ISendMessage
from modules.content_ia.use_cases.dto import UserType
from .interfaces.i_send_prompt import ISendPrompt

class ChatIAUseCase:

    def __init__(self, 
        search_content_repository: SearchContentRepository, 
        ia: IA,
        save_response_repo: ISaveResponseIa,
        factory_user_repository: FactoryUserRepository,
        factory_send_message: ISendMessage,
        factory_send_prompt: ISendPrompt
        ):
        self.search_content_repository = search_content_repository
        self.ia = ia
        self.save_response_repo = save_response_repo
        self.factory_user_repository = factory_user_repository
        self.plan_config = None
        self.content = None
        self.factory_send_message = factory_send_message
        self.factory_send_prompt = factory_send_prompt
    def chatWithContentIa(self, content_id: int, question: str, user_id: int) -> Content:
        """
        1.-Recibir el id del usuario
        2.-Obtener tipo de usuario por plan
        3.-Revisar en el plan cuantos mensajes puede enviar a la IA
        3.-Dependiendo del tipo de usuario debe tener un prompt diferente para la respuesta de la IA        
        """

        user_type = None
        if self.plan_config is None:
            user_repository = self.factory_user_repository.create_using_mode(os.getenv("MODE"))
            print("user_repository", user_id)
            user_type = user_repository.get_user_type(user_id)
            self.plan_config = user_repository.get_user_type_plan_config(user_type)
        

        if self.content is None:
            self.content = self.search_content_repository.get_content(content_id)
        comments = self.content.comments

        if user_type is not None:
            print("user_type", user_type)
            f_send_message = self.factory_send_message.create(user_type)
            send_message = f_send_message.send_message(question, self.plan_config, len(comments))        
        
            f_send_prompt = self.factory_send_prompt.create(user_type)
            response_text = f_send_prompt.send_prompt(comments, question, self.ia)

            messages = self.save_response_repo.save_response(response_text)

            print(messages, "messages")
