from ..factory_user_content import FactoryCreatorUserContent
from ..user_repository import FactoryUserRepository
from modules.content_ia.use_cases.generate_content_use_case.generate_content_use_case import GenerateContentUseCase

def create_generate_content_use_case():
    factory_creator_user_content = FactoryCreatorUserContent()
    factory_user_repository = FactoryUserRepository()
    return GenerateContentUseCase(
        factory_creator_user_content, 
        factory_user_repository
    )
