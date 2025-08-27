from modules.content_ia.use_cases.dto import Content, Error
from .interfaces import FactoryCreatorUserContent, FactoryUserRepository
from ..dto import SourceType
import os


class GenerateContentUseCase:

  def __init__(self, 
              factory_creator_user_content:FactoryCreatorUserContent, 
              factory_user_repository:FactoryUserRepository,
  ):
    self.factory_creator_user_content = factory_creator_user_content
    self.factory_user_repository = factory_user_repository

  def process_content(self, source_path:str, user_id:int, source_type:SourceType) -> Content:
    all_results = []

    user_repository = self.factory_user_repository.create_using_mode(os.getenv("MODE"))

    user_type = user_repository.get_user_type(user_id)
    plan_config = user_repository.get_user_type_plan_config(user_type)
  
    factory_user_content = self.factory_creator_user_content.create(user_type)

    content_generator = factory_user_content.create_content_generator(source_type) # PDF
    content_repository = factory_user_content.create_content_repository()

    instances_plan_config = factory_user_content.create_using_plan_config(plan_config)

    workflow = instances_plan_config.workflow
    notifier = instances_plan_config.notifier
    all_ias = instances_plan_config.ias

    user_email = content_repository.get_user_email(user_id)

    for ia in all_ias:
      try:
        content_generator.set_ia(ia)
        content = content_generator.generate_content(source_path)
        content_saved = content_repository.save_content(content)
        all_results.append(content_saved)
        print(content_saved)
      except Exception as e:
        error = Error(message=str(e), title="Error al procesar contenido", module="ContentUseCase")
        content_repository.save_error(error)
        print(f"Error al procesar contenido: {e}")
  
    notifier.send_email(user_email)
    workflow.after_process(user_id)
    return all_results





