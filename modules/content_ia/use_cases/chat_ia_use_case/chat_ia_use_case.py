from .interfaces import SearchContentRepository
from ..shared.base_ia import IA, IAMessage

class ChatIAUseCase:

  def __init__(self, search_content_repository: SearchContentRepository, ia: IA):
    self.search_content_repository = search_content_repository
    self.ia = ia
  
  def send_message(self, content_id: int, message:str) -> str:
    """
    1. Obtener el contenido usando el content_id
    2. Extraer los comentarios del contenido
    3. Construir un prompt con mensaje de usuario y comentarios
    4. Enviar el prompt a la IA
    5. Retornar la respuesta de la IA
    """

    """
    1. search_content_repository.get_content_by_id(content_id)
    2. ChatIAUseCase
    3. ChatIAUseCase
    4. ia.send_message(prompt)
    5. ChatIAUseCase
    """
    content = self.search_content_repository.get_content(content_id)
    comments = content.comments
    prompt = f"""
    Del siguiente contenido
    {comments}
    El usuario tiene el siguiente mensaje
    {message}
    Responde a su mensaje
    """
    messages = [
      IAMessage(role="user", content=prompt)
    ]
    response = self.ia.send_prompt(messages, is_json=False)
    return response.content