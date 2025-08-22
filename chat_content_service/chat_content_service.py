from dto import SubcontentType, IANames
from utility.ia import GeminiIA, ClaudeIA, IA, IAMessage
from content_service.content_repository import ContentRepository

class ChatContentService:

  def __init__(self, chat_content_repository: ContentRepository):
    self.chat_content_repository = chat_content_repository

  def chat_with_content(self, video_content_id:int, subcontent_type:SubcontentType, message:str, ia_name:IANames):
    """
    Obtener el contenido del video por medio del id
    Obtener el subcontenido por medio del atributo de video
    Enviar mensaje a la IA
    """
    video_content = self.chat_content_repository.get_content(video_content_id)
    attributes = {
      SubcontentType.SUMMARY.value: video_content.summary,
      SubcontentType.QUESTION.value: video_content.questions,
      SubcontentType.ANSWER.value: video_content.answers,
      SubcontentType.TOPIC.value: video_content.topics,
      SubcontentType.COMMENTS.value: video_content.comments
    }
    attribute_value = attributes[subcontent_type.value]
    prompt = f"""
      El usuario te ha enviado el siguiente mensaje: {message}
      El contenido del video es el siguiente: {attribute_value}
    """
    ia = ClaudeIA() if ia_name.value == IANames.CLAUDE.value else GeminiIA()
    response = self._send_prompt(prompt, is_json=False, ia=ia)
    print("LA RESPUESTA --------------------------------")
    print(response)
    return response



  """
  Objetivo: Enviar prompt a la IA
  Solo va a cambiar cuando la lógica de envío de prompt a la IA cambie
  """
  def _send_prompt(self, prompt:str, is_json:bool, ia: IA) -> str:
    messages = [
      IAMessage(role="user", content=prompt)
    ]
    response = ia.send_prompt(messages, is_json)
    return response.content

      