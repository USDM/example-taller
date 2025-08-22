from .factory_user_content import FactoryUserContent
from ..content_video_generator import FreeContentVideoGenerator
from ..content_repository import NullRepository
from ..notifier import NullEmail, SubsNotifier
from ..workflow import NullWorkflow, SubsWorkFlow
from utility.ia import GeminiIA
from dto import PlanConfig
from utility.ia import FactoryIA

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