from .factory_user_content import FactoryUserContent
from ..content_generator.video import SuscribeContentVideoGenerator
from ..content_repository import DatabaseRepository
from ..notifier import SubsNotifier
from ..workflow import NullWorkflow
from ..ia import ClaudeIA, GeminiIA
from modules.content_ia.use_cases.dto import SourceType

class SuscribeFactoryUserContent(FactoryUserContent):

  def create_content_generator(self, source_type:SourceType):
    return SuscribeContentVideoGenerator()
  
  def create_content_repository(self):
    return DatabaseRepository()
  
  def create_notifier(self):
    return SubsNotifier()
  
  def create_workflow(self):
    return NullWorkflow()
  
  def create_all_ias(self):
    return [ClaudeIA(), GeminiIA()]