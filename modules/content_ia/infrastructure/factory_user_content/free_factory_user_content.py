from .factory_user_content import FactoryUserContent
from ..content_generator.video import FreeContentVideoGenerator
from ..content_repository import NullRepository
from ..notifier import NullEmail
from ..workflow import NullWorkflow
from ..ia import GeminiIA
from modules.content_ia.use_cases.dto import SourceType
from ..content_generator.pdf import FreeContentPDFGenerator

class FreeFactoryUserContent(FactoryUserContent):

  def create_content_generator(self, source_type:SourceType):
    if source_type.value == SourceType.VIDEO.value:
      return FreeContentVideoGenerator()
    elif source_type.value == SourceType.PDF.value:
      return FreeContentPDFGenerator()
    else:
      raise ValueError(f"Source type {source_type} not supported")
  
  def create_content_repository(self):
    return NullRepository()
  
  def create_notifier(self):
    return NullEmail()
  
  def create_workflow(self):
    return NullWorkflow()
  
  def create_all_ias(self):
    return [GeminiIA()]