from modules.content_ia.use_cases.dto import VideoContent, Error
from modules.content_ia.use_cases.generate_content_use_case.interfaces import ContentRepository
"""
Objetivo: Guardar contenido de video en base de datos
Solo va a cambiar cuando la lógica de guardado de contenido de video cambie
"""
class NullRepository(ContentRepository):

  def __init__(self):
    pass

  def save_content(self, content_video:VideoContent) -> VideoContent:
    return content_video
  

  def get_content(self, id:int) -> VideoContent:
    return None
  

  def update_content(self, content_video:VideoContent):
    pass


  def save_error(self, error:Error):
    pass
  
  def get_all_errors(self) -> list[Error]:
    return []
  
  def get_user_email(self, user_id:int) -> str:
    return ""
  
