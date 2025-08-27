from abc import ABC, abstractmethod
from modules.content_ia.use_cases.dto import Content, SubcontentType

class BaseContentGenerator(ABC):
  
  @abstractmethod
  def generate_content(self, source_path:str) -> Content:
    pass

  @abstractmethod
  def generate_subcontent(self, content:Content, subcontent_type:SubcontentType) -> Content:
    pass