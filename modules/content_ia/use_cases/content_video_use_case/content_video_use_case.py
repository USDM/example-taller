from modules.content_ia.use_cases.dto import VideoContent, Error
from .interfaces import FactoryCreatorUserContent, FactoryUserRepository
import os


class ContentVideoUseCase:

  def __init__(self, 
              factory_creator_user_content:FactoryCreatorUserContent, 
              factory_user_repository:FactoryUserRepository,
  ):
    self.factory_creator_user_content = factory_creator_user_content
    self.factory_user_repository = factory_user_repository

  def process_content_video(self, video_url:str, user_id:int) -> VideoContent:
    all_results = []

    user_repository = self.factory_user_repository.create_using_mode(os.getenv("MODE"))

    user_type = user_repository.get_user_type(user_id)
    plan_config = user_repository.get_user_type_plan_config(user_type)
  
    factory_user_content = self.factory_creator_user_content.create(user_type)

    content_video_generator = factory_user_content.create_content_video_generator()
    content_repository = factory_user_content.create_content_repository()

    instances_plan_config = factory_user_content.create_using_plan_config(plan_config)

    workflow = instances_plan_config.workflow
    notifier = instances_plan_config.notifier
    all_ias = instances_plan_config.ias

    user_email = content_repository.get_user_email(user_id)

    for ia in all_ias:
      try:
        content_video_generator.set_ia(ia)
        content_video = content_video_generator.generate_content_video(video_url)
        content_video_saved = content_repository.save_content(content_video)
        all_results.append(content_video_saved)
        print(content_video_saved)
      except Exception as e:
        error = Error(message=str(e), title="Error al procesar contenido de video", module="ContentVideoUseCase")
        content_repository.save_error(error)
        print(f"Error al procesar contenido de video: {e}")
  
    notifier.send_email(user_email)
    workflow.after_process(user_id)
    return all_results





