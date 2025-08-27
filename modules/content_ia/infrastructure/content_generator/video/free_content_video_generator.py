from modules.content_ia.use_cases.dto import VideoContent, VideoMetadata, VideoComment, VideoCommentRating, SubcontentType
from .subtitle_extractor import SubtitleExtractor
from modules.content_ia.use_cases.shared import IA, IAMessage
from modules.content_ia.use_cases.generate_content_use_case.interfaces import BaseContentGenerator

"""
Objetivo: Generar contenido de video
Solo va a cambiar cuando la lógica de generación de contenido de video cambie
"""

class FreeContentVideoGenerator(BaseContentGenerator):

  AMOUNT_COMMENTS = 5

  def __init__(self):
    self.ia = None

  def set_ia(self, ia:IA):
    self.ia = ia

  """
  Objetivo: Generar subcontenido del video
  Solo va a cambiar cuando la lógica de generación de subcontenido cambie
  """
  def generate_subcontent(self, content_video:VideoContent, subcontent_type:SubcontentType):    
    methods = {
        SubcontentType.COMMENTS.value: lambda: setattr(content_video, 'comments', self._get_comments(content_video.text, perspective="economico"))
    }
    methods[subcontent_type.value]()
    return content_video

  """
  Objetivo: Generar contenido de video
  Solo va a cambiar cuando la lógica de generación de contenido de video cambie
  """
  def generate_content(self, video_url:str) -> VideoContent:
    subtitles = self._get_subtitles(video_url)
    formatted_subtitles = self._format_subtitles(subtitles)
    metadata = self._get_metadata(formatted_subtitles)
    comments = self._get_comments(formatted_subtitles, perspective="economica")
    return VideoContent(
      text=formatted_subtitles,
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
  Objetivo: Obtener subtitulos del video
  Solo va a cambiar cuando la lógica de obtención de subtitulos cambie
  """
  def _get_subtitles(self, video_url:str):
    subtitle_extractor = SubtitleExtractor()
    subtitles = subtitle_extractor.extract_subtitles(video_url)
    return subtitles
  
  """
  Objetivo: Formatear subtitulos
  Solo va a cambiar cuando la lógica de formateo de subtitulos cambie
  """
  def _format_subtitles(self, subtitles:str):
    prompt = f"""
    Formatea los siguientes subtitulos para formato entrevista usando html
    El formato debe seguir el formato:
    person_name: text_person_name
    Subtitulos: {subtitles}
    """
    response = self._send_prompt(prompt, is_json=False)
    return response
  

  """
  Objetivo: Obtener metadata del video
  Solo va a cambiar cuando la lógica de obtención de metadata cambie
  """
  def _get_metadata(self, subtitles:str) -> VideoMetadata:
    prompt = f"""
    Dado los siguientes subtitulos: {subtitles}
    Obtén el titulo y autores
    En el siguiente format JSON:
    {{
      "title": "Titulo del video, en caso de no tener crea un titulo de acuerdo al contenido del video",
      "authors": ["nombres de los autores del video, si desconoces a algun autor no lo incluyas"]
    }}
    """
    response = self._send_prompt(prompt, is_json=True)
    video_metadata = VideoMetadata(
      title=response["title"], 
      authors=response["authors"]
    )
    return video_metadata
  

  def _get_comments(self, subtitles:str, perspective:str) -> list[VideoComment]:
    json_format = """
    [{
      "comment": "comentario del video, no incluyas caracteres especiales, solo letras y numeros",
      "reasoning": "razonamiento sobre el comentario"
      "rating": "rating del comentario con las siguientes opciones: positive, negative, neutral"
    }]
    """
    prompt = f"""
    Analiza los subtitulos que te voy a pasar y genera {self.AMOUNT_COMMENTS} comentarios del video
    Con un enfoque de {perspective}
    El formato debe seguir el formato:
    {json_format}
    Subtitulos: {subtitles}
    """
    response = self._send_prompt(prompt, is_json=True)
    video_comments = [
      VideoComment(
      text=comment["comment"], 
      reasoning=comment["reasoning"], 
      rating=VideoCommentRating(comment["rating"])
    ) 
    for comment in response]
    return video_comments
  
  
  """
  Objetivo: Enviar prompt a la IA
  Solo va a cambiar cuando la lógica de envío de prompt a la IA cambie
  """
  def _send_prompt(self, prompt:str, is_json:bool) -> str:
    messages = [
      IAMessage(role="user", content=prompt)
    ]
    response = self.ia.send_prompt(messages, is_json)
    return response.content