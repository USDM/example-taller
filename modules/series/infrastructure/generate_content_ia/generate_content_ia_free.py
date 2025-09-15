from ...use_cases.dto import ContentSerie
from ...use_cases.dto import LastSerieDataInfo, WindowIndicatorData, WindowIndicatorType
from ...use_cases.generate_content_use_case.interfaces import GenerateContentIAInterface
from ..ia.gemini import GeminiIA
from ...use_cases.shared.base_ia import IAMessage

class GenerateContentIAFree(GenerateContentIAInterface):

    def generate_content(self, serie_info:LastSerieDataInfo) -> ContentSerie:
        prompt = f"""
        Dado el ultimo dato de la serie y su nombre.
        Obtén comentarios, resumen y proyecciones.
        Datos:
        {serie_info}
        En el siguiente format JSON:
        {{
        "comments": ["comentario 1", "comentario 2"],
        "summary": "resumen de la serie",
        "projections": "proyecciones a futuro de la serie"
        }}
        Solo responde con el json
        """
        response = self._send_prompt(prompt, is_json=True)
        content_serie = ContentSerie(
            comments=response["comments"],
            summary=response["summary"],
            projections=response["projections"]
        )
        return content_serie

    
    def generate_content_with_indicator(self, serie_info:LastSerieDataInfo, last_indicator_data: WindowIndicatorData, type_indicator: WindowIndicatorType) -> ContentSerie:
        prompt = f"""
        Dado el ultimo dato de la serie y su nombre, como tambien su indicador y su ultimo dato del calculo del inidicador.
        Obtén comentarios, resumen y proyecciones.
        Datos:
        {serie_info}
        En el siguiente format JSON:
        {{
        "comments": ["comentario 1", "comentario 2"]
        }}
        IMPORTANTE
        -Tienes un limite de 200 caracteres de respusta por cada comments
        Solo responde con el json
        """
        response = self._send_prompt(prompt, is_json=True)
        content_serie = ContentSerie(
            comments=response["comments"]
        )
        return content_serie


    def _send_prompt(self, prompt:str, is_json:bool) -> str:
        messages = [
            IAMessage(role="user", content=prompt)
        ]
        response = GeminiIA().send_prompt(messages, is_json)
        return response.content