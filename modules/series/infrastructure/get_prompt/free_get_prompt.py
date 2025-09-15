from ...use_cases.dto import LastSerieDataInfo, WindowIndicatorType
from .generate_content_indicator_use_case.interfaces import GetPromptInterface


class FreeGetPrompt(GetPromptInterface):
    def get_prompt(self, last_serie_data:LastSerieDataInfo, indicators_info:list[WindowIndicatorType]) -> str:
        prompt = f"""
        PROMPT PARA FREE
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
        return prompt