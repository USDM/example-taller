from ...use_cases.dto import LastSerieDataInfo, WindowIndicatorType
from ...use_cases.generate_content_indicator_use_case.interfaces import GetPromptInterface


class StudentGetPrompt(GetPromptInterface):
    def get_prompt(self, last_serie_data:LastSerieDataInfo, indicators_info:list[WindowIndicatorType]) -> str:
        prompt = f"""
        PROMPT PARA STUDENT
        Dado el ultimo dato de la serie y su nombre y los indicadores.
        Obtén comentarios, resumen, proyecciones, confianza, riesgo y tendencia.
        Datos:
        {last_serie_data}
        {indicators_info}
        En el siguiente format JSON:
        {{
        "comments": ["comentario 1", "comentario 2"],
        "summary": "resumen de la serie",
        "projections": "proyecciones a futuro de la serie",
        "confidence": "confianza en la proyeccion",
        "risk": "riesgo de la proyeccion",
        "trend": "tendencia de la proyeccion",
        }}
        Solo responde con el json
        """
        return prompt