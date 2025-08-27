from modules.content_ia.use_cases.dto import SubcontentType, ContentMetadata
from modules.content_ia.use_cases.dto import (
  ContentMetadata,
  ContentComment,
  ContentCommentRating,
  Content
  )
from modules.content_ia.use_cases.shared import IA, IAMessage
from modules.content_ia.use_cases.generate_content_use_case.interfaces import BaseContentGenerator

"""
Objetivo: Generar contenido de video
Solo va a cambiar cuando la lógica de generación de contenido de video cambie
"""

class FreeContentPDFGenerator(BaseContentGenerator):

  AMOUNT_COMMENTS = 5

  def __init__(self):
    self.ia = None

  def set_ia(self, ia:IA):
    self.ia = ia

  """
  Objetivo: Generar subcontenido del video
  Solo va a cambiar cuando la lógica de generación de subcontenido cambie
  """
  def generate_subcontent(self, content_video:Content, subcontent_type:SubcontentType):    
    methods = {
        SubcontentType.COMMENTS.value: lambda: setattr(content_video, 'comments', self._get_comments(content_video.text, perspective="economico"))
    }
    methods[subcontent_type.value]()
    return content_video

  """
  Objetivo: Generar contenido de video
  Solo va a cambiar cuando la lógica de generación de contenido de video cambie
  """
  def generate_content(self, source_path:str) -> Content:
    text_pdf = self._format_text_pdf(source_path)
    metadata = self._get_metadata(source_path)
    comments = self._get_comments(source_path, perspective="economica")
    return Content(
      text=text_pdf,
      metadata=metadata,
      comments=comments,
      summary="",
      questions=[],
      answers=[],
      topics=[],
      ia_name=self.ia.get_ia_name(),
      critical_perspective="",
      sources=[]
    )
  
  """
  Objetivo: Formatear subtitulos
  Solo va a cambiar cuando la lógica de formateo de subtitulos cambie
  """
  def _format_text_pdf(self, source_path:str):
    prompt = f"""
    Formatea el texto de un pdf en html que sea legible para el usuario
    """
    response = self._send_prompt(prompt, source_path=source_path, is_json=False)
    return response
  


  """
  Objetivo: Obtener metadata del video
  Solo va a cambiar cuando la lógica de obtención de metadata cambie
  """
  def _get_metadata(self, source_path:str) -> ContentMetadata:
    prompt = f"""
    Dado el pdf
    Obtén el titulo y autores
    En el siguiente format JSON:
    {{
      "title": "Titulo del video, en caso de no tener crea un titulo de acuerdo al contenido del video",
      "authors": ["nombres de los autores del video, si desconoces a algun autor no lo incluyas"]
    }}
    """
    response = self._send_prompt(prompt, source_path=source_path, is_json=True)
    content_metadata = ContentMetadata(
      title=response["title"], 
      authors=response["authors"]
    )
    return content_metadata

  

  def _get_comments(self, source_path:str, perspective:str) -> list[ContentComment]:
    json_format = """
    [{
      "comment": "comentario del video, no incluyas caracteres especiales, solo letras y numeros",
      "reasoning": "razonamiento sobre el comentario"
      "rating": "rating del comentario con las siguientes opciones: positive, negative, neutral"
    }]
    """
    prompt = f"""
    Analiza el pdf que te voy a pasar y genera {self.AMOUNT_COMMENTS} comentarios del pdf
    Con un enfoque de {perspective}
    El formato debe seguir el formato:
    {json_format}
    """
    response = self._send_prompt(prompt, source_path=source_path, is_json=True)
    content_comments = [
      ContentComment(
      text=comment["comment"], 
      reasoning=comment["reasoning"], 
      rating=ContentCommentRating(comment["rating"])
    ) 
    for comment in response]
    return content_comments
  
  
  """
  Objetivo: Enviar prompt a la IA
  Solo va a cambiar cuando la lógica de envío de prompt a la IA cambie
  """
  def _send_prompt(self, prompt:str, source_path:str, is_json:bool) -> str:
    archivo_pdf = self.ia.create_file_from_path(
        file_path=source_path,
        mime_type="application/pdf",
        name=source_path
    )
    
    mensaje = self.ia.create_user_message_with_files(
        content=prompt,
        files=[archivo_pdf]
    )
    
    response = self.ia.send_prompt_with_files(
        messages=[mensaje], 
        is_json=is_json
    )
    
    return response.content