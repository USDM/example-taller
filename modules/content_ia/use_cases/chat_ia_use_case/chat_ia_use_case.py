from modules.content_ia.use_cases.dto import Content
from .interfaces.search_content_repository import SearchContentRepository
from .interfaces.i_save_response_ia import ISaveResponseIa
from .interfaces.validate_total_messages import ValidateTotalMessagesInterface
from modules.content_ia.use_cases.shared.base_ia import IA, IAMessage
from modules.content_ia.use_cases.dto import UserType
from modules.content_ia.infrastructure.get_prompt.factory_get_prompt import FactoryGetPrompt

class ChatIAUseCase:

    def __init__(self, 
        search_content_repository: SearchContentRepository, 
        ia: IA,
        save_response_repo: ISaveResponseIa,
        validate_total_messages_repo: ValidateTotalMessagesInterface,
        get_prompt_factory: FactoryGetPrompt
    ):
        self.search_content_repository = search_content_repository
        self.ia = ia
        self.save_response_repo = save_response_repo
        self.validate_total_messages_repo = validate_total_messages_repo
        self.get_prompt_factory = get_prompt_factory

    def chatWithContentIa(self, content_id: int, question: str, user_type: UserType) -> str:

        if not self.validate_total_messages_repo.validate_total_messages(user_type):
            return "You have reached the maximum number of messages"

        content = self.search_content_repository.get_content(content_id)
        comments = content.comments

        get_prompt_factory = self.get_prompt_factory.create(user_type)
        prompt = get_prompt_factory.get_prompt(comments, question)

        messages = [
            IAMessage(role="user", content=prompt)
        ]

        response = self.ia.send_prompt(messages, is_json=False)
        response_text = response.content 

        self.save_response_repo.save_response({"message": question, "response": response_text})

        pass