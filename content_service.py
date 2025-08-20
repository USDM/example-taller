from content_video_generator import ContentVideoGenerator
from content_repository import ContentRepository
from dto import VideoContent, SubcontentType, Error

"""
VAMOS A SUPONER QUE NOS LLEGAN NUEVOS REQUERIMIENTOS

1. GENERAR SOLO COMENTARIOS Y LO DEMAS A DECISION DEL USUARIO
2. GUARDAR LOS ERRORES EN BASE DE DATOS
3. CHATEAR CON EL CONTENIDO QUE EL USUARIO DECIDA

"""

"""
Objetivo: Resolver solicitudes de contenido de video
Solo va a cambiar cuando la lógica de  las solicitudes de contenido de video cambien
"""

class ContentService:

  def __init__(self):
    self.content_video_generator = ContentVideoGenerator()
    self.content_repository = ContentRepository()

  def get_all_errors(self) -> list[Error]:
    return self.content_repository.get_all_errors()
  
  """
  Objetivo: Procesar contenido de video
  Solo va a cambiar cuando la lógica de procesamiento de contenido de video cambie
  """
  def process_content_video(self, video_url:str) -> VideoContent:
    try:
      content_video = self.content_video_generator.generate_content_video(video_url)
      content_video_saved = self.content_repository.save_content(content_video)
      print(content_video_saved)
      return content_video_saved
    except Exception as e:
      error = Error(message=str(e), title="Error al procesar contenido de video", module="ContentService")
      self.content_repository.save_error(error)

  """
  Objetivo: Generar subcontenido del video
  Solo va a cambiar cuando la lógica de generación de subcontenido cambie
  """
  def generate_video_subcontent(self, video_content_id:int, subcontent_type:SubcontentType):
    try:
      video_content = self.content_repository.get_content(video_content_id)
      updated_video_content = self.content_video_generator.generate_subcontent(video_content, subcontent_type)
      self.content_repository.update_content(updated_video_content)
      print("--------------------------------")
      print(updated_video_content)
      return updated_video_content
    except Exception as e:
      error = Error(message=str(e), title="Error al generar subcontenido del video", module="ContentService")
      self.content_repository.save_error(error)
  






