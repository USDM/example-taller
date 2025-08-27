from .factory_user_content import FactoryUserContent
from ..content_video_generator import FreeContentVideoGenerator
from ..content_repository import NullRepository
from ..notifier import NullEmail
from ..workflow import NullWorkflow
from ..ia import GeminiIA

class FreeFactoryUserContent(FactoryUserContent):

  def create_content_video_generator(self):
    return FreeContentVideoGenerator()
  
  def create_content_repository(self):
    return NullRepository()
  
  def create_notifier(self):
    return NullEmail()
  
  def create_workflow(self):
    return NullWorkflow()
  
  def create_all_ias(self):
    return [GeminiIA()]