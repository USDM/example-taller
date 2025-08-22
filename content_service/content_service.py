from .content_video_generator import BaseContentVideoGenerator
from .content_repository.content_repository import ContentRepository
from dto import VideoContent, SubcontentType, Error, IANames, UserType
from utility.ia import GeminiIA, ClaudeIA, FactoryIA
from .content_video_generator import FactoryContentVideoGenerator
from .content_repository.factory_repository import FactoryRepository
from .notifier import NotifierFactory
from .workflow import FactoryWorkflow
from .factory_user_content import FactoryUserContent
from .factory_user_content import FactoryCreatorUserContent
from .user_repository import UserRepository
from .user_repository import FactoryUserRepository
import os
"""
Objetivo: Resolver solicitudes de contenido de video
Solo va a cambiar cuando la lógica de  las solicitudes de contenido de video cambien
"""


class ContentService:

  """
  Objetivo: Procesar contenido de video
  Solo va a cambiar cuando la lógica de procesamiento de contenido de video cambie
  """
  def process_content_video(self, video_url:str, user_id:int) -> VideoContent:
    all_results = []

    user_repository = FactoryUserRepository().create_using_mode(os.getenv("MODE"))

    user_type = user_repository.get_user_type(user_id)
    plan_config = user_repository.get_user_type_plan_config(user_type)
  
    factory_user_content = FactoryCreatorUserContent.create(user_type)

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
        error = Error(message=str(e), title="Error al procesar contenido de video", module="ContentService")
        content_repository.save_error(error)
        print(f"Error al procesar contenido de video: {e}")
  
    notifier.send_email(user_email)
    workflow.after_process(user_id)
    return all_results

  """
  Objetivo: Generar subcontenido del video
  Solo va a cambiar cuando la lógica de generación de subcontenido cambie
  """
  def generate_video_subcontent(self, video_content_id:int, subcontent_type:SubcontentType, user_type:UserType):
    try:
      content_video_generator = FactoryContentVideoGenerator.create(user_type)
      content_repository = FactoryRepository.create(user_type)
      video_content = content_repository.get_content(video_content_id)
      ia = FactoryIA.create(video_content.ia_name) #ClaudeIA() if video_content.ia_name == IANames.CLAUDE.value else GeminiIA()
      content_video_generator.set_ia(ia)
      updated_video_content = content_video_generator.generate_subcontent(video_content, subcontent_type)
      content_repository.update_content(updated_video_content)
      print("--------------------------------")
      print(updated_video_content)
      return updated_video_content
    except Exception as e:
      error = Error(message=str(e), title="Error al generar subcontenido del video", module="ContentService")
      content_repository.save_error(error)






