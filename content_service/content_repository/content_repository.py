from dto import VideoContent, Error
from typing import Protocol

"""
Objetivo: Guardar contenido de video en base de datos
Solo va a cambiar cuando la lógica de guardado de contenido de video cambie
"""
class ContentRepository(Protocol):

  def save_content(self, content_video:VideoContent) -> VideoContent:
    pass
  

  def get_content(self, id:int) -> VideoContent:
    pass
  

  def update_content(self, content_video:VideoContent):
    pass

  def save_error(self, error:Error):
    pass
  
  def get_all_errors(self) -> list[Error]:
    pass
  
  def get_user_email(self, user_id:int) -> str:
    pass
