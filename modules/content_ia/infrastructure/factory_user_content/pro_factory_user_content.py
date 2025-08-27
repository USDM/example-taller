from .factory_user_content import FactoryUserContent
from ..content_generator.video import ProContentVideoGenerator
from ..content_repository import DatabaseRepository
from ..notifier import SubsNotifier
from ..workflow import SubsWorkFlow
from ..ia import ClaudeIA, GeminiIA, ChatGPT
from modules.content_ia.use_cases.dto import SourceType

class ProFactoryUserContent(FactoryUserContent):

  def create_content_generator(self, source_type:SourceType):
    return ProContentVideoGenerator()
  
  def create_content_repository(self):
    return DatabaseRepository()
  
  def create_notifier(self):
    return SubsNotifier()
  
  def create_workflow(self):
    return SubsWorkFlow()
  
  def create_all_ias(self):
    return [ClaudeIA(), GeminiIA(), ChatGPT()]
