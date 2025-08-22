from dto import VideoContent, Error
from .content_repository import ContentRepository
"""
Objetivo: Guardar contenido de video en base de datos
Solo va a cambiar cuando la lógica de guardado de contenido de video cambie
"""
class DatabaseRepository(ContentRepository):

  def __init__(self):
    self.memory = {}
    self.errores = {}

  def save_content(self, content_video:VideoContent) -> VideoContent:
    id = len(self.memory) + 1
    self.memory[id] = content_video
    content_video.id = id
    return content_video
  

  def get_content(self, id:int) -> VideoContent:
    return self.memory[id]
  

  def update_content(self, content_video:VideoContent):
    self.memory[content_video.id] = content_video


  def save_error(self, error:Error):
    id = len(self.errores) + 1
    self.errores[id] = error
    error.id = id
    return error
  
  def get_all_errors(self) -> list[Error]:
    return list(self.errores.values())
  
  def get_user_email(self, user_id:int) -> str:
    return "test@test.com"
  
