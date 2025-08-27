from .factory_user_content import FactoryUserContent
from ..content_generator.video import SuscribeContentVideoGenerator
from ..content_generator.pdf import StudentContentPDFGenerator
from ..content_generator.tweet import FreeContentTweetGenerator
from ..content_repository import DatabaseRepository
from ..notifier import SubsNotifier
from ..workflow import SubsWorkFlow
from ..ia import ClaudeIA, GeminiIA
from modules.content_ia.use_cases.dto import SourceType

class StudentFactoryUserContent(FactoryUserContent):

  def create_content_generator(self, source_type:SourceType):
    if source_type.value == SourceType.VIDEO.value:
      return SuscribeContentVideoGenerator()
    elif source_type.value == SourceType.PDF.value:
      return StudentContentPDFGenerator()
    elif source_type.value == SourceType.TWEET.value:
      return FreeContentTweetGenerator()
    else:
      raise ValueError(f"Source type {source_type} not supported")
  
  def create_content_repository(self):
    return DatabaseRepository()
  
  def create_notifier(self):
    return SubsNotifier()
  
  def create_workflow(self):
    return SubsWorkFlow()
  
  def create_all_ias(self):
    return [ClaudeIA(), GeminiIA()]