from ...use_cases.dto import LastSerieDataInfo, WindowIndicatorType
from ...use_cases.generate_content_indicator_use_case.interfaces import GetPromptInterface


class FreeGetPrompt(GetPromptInterface):
    def get_prompt(self, last_serie_data:LastSerieDataInfo, indicators_info:list[WindowIndicatorType]) -> str:
        prompt = f"""
        PROMPT PARA FREE
        Dado el ultimo dato de la serie y su nombre y los indicadores.
        Obtén comentarios.
        Datos:
        {last_serie_data}
        {indicators_info}
        En el siguiente format JSON:
        {{
        "comments": ["comentario 1", "comentario 2"]
        }}
        Solo responde con el json
        """
        return prompt