from .factory_user_content import FactoryUserContent
from ..content_video_generator import SuscribeContentVideoGenerator
from ..content_repository import DatabaseRepository
from ..notifier import SubsNotifier
from ..workflow import NullWorkflow
from utility.ia import ClaudeIA, GeminiIA

class SuscribeFactoryUserContent(FactoryUserContent):

  def create_content_video_generator(self):
    return SuscribeContentVideoGenerator()
  
  def create_content_repository(self):
    return DatabaseRepository()
  
  def create_notifier(self):
    return SubsNotifier()
  
  def create_workflow(self):
    return NullWorkflow()
  
  def create_all_ias(self):
    return [ClaudeIA(), GeminiIA()]