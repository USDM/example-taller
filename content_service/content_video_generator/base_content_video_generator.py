from abc import ABC, abstractmethod
from dto import VideoContent, SubcontentType

class BaseContentVideoGenerator(ABC):
  
  @abstractmethod
  def generate_content_video(self, video_url:str) -> VideoContent:
    pass

  @abstractmethod
  def generate_subcontent(self, content_video:VideoContent, subcontent_type:SubcontentType) -> VideoContent:
    pass