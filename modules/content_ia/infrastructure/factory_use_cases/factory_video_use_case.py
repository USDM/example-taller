from ..factory_user_content import FactoryCreatorUserContent
from ..user_repository import FactoryUserRepository
from modules.content_ia.use_cases.content_video_use_case.content_video_use_case import ContentVideoUseCase

def create_content_service():
    factory_creator_user_content = FactoryCreatorUserContent()
    factory_user_repository = FactoryUserRepository()
    return ContentVideoUseCase(
        factory_creator_user_content, 
        factory_user_repository
    )
