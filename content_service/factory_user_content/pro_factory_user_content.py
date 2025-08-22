from .factory_user_content import FactoryUserContent
from ..content_video_generator import ProContentVideoGenerator
from ..content_repository import DatabaseRepository
from ..notifier import SubsNotifier
from ..workflow import SubsWorkFlow
from utility.ia import ClaudeIA, GeminiIA, ChatGPT

class ProFactoryUserContent(FactoryUserContent):

  def create_content_video_generator(self):
    return ProContentVideoGenerator()
  
  def create_content_repository(self):
    return DatabaseRepository()
  
  def create_notifier(self):
    return SubsNotifier()
  
  def create_workflow(self):
    return SubsWorkFlow()
  
  def create_all_ias(self):
    return [ClaudeIA(), GeminiIA(), ChatGPT()]
