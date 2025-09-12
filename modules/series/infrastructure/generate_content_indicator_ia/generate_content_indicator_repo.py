from ...use_cases.generate_content_indicator_use_case.interfaces import IGenerateContentIndicatorIA
from ...use_cases.dto import LastSerieDataInfo
from ..ia.gemini import GeminiIA
from ...use_cases.shared.base_ia import IAMessage
from ...use_cases.dto import WindowIndicatorType
from ...use_cases.dto import ContentSerie

class GenerateContentIndicatorIA(IGenerateContentIndicatorIA):
    def generate_content_indicator_ia(self, last_serie_data:LastSerieDataInfo, indicators_info:list[WindowIndicatorType]) -> ContentSerie:
        prompt = f"""
        Dado el ultimo dato de la serie y su nombre y los indicadores.
        Obtén comentarios, resumen y proyecciones.
        Datos:
        {last_serie_data}
        {indicators_info}
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


    def _send_prompt(self, prompt:str, is_json:bool) -> str:
        messages = [
            IAMessage(role="user", content=prompt)
        ]
        response = GeminiIA().send_prompt(messages, is_json)
        return response.content