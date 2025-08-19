from content_video_generator import ContentVideoGenerator
from content_repository import ContentRepository
from dto import VideoContent
"""
Objetivo: Resolver solicitudes de contenido de video
Solo va a cambiar cuando la lógica de  las solicitudes de contenido de video cambien
"""

class ContentService:

  def __init__(self):
    self.content_video_generator = ContentVideoGenerator()
    self.content_repository = ContentRepository()
  
  """
  Objetivo: Procesar contenido de video
  Solo va a cambiar cuando la lógica de procesamiento de contenido de video cambie
  """
  def process_content_video(self, video_url:str):
    content_video = self.content_video_generator.generate_content_video(video_url)
    print(content_video)
    self.content_repository.save_content(content_video)






