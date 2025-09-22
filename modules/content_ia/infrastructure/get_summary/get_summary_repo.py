from modules.content_ia.use_cases.summary_use_case.interface.get_summary import GetSummaryInterface
from modules.content_ia.use_cases.shared.base_ia import IA, IAMessage
from modules.common.tables import TableResponseIa


class GetSummaryRepo(GetSummaryInterface):
    def get_summary(self, ia: IA, history: list[dict]) -> str:
        prompt = f"""
        Dado el historial de conversacion: {history}
        Genera un resumen de la conversacion
        """

        messages = [
            IAMessage(role="user", content=prompt)
        ]

        response = ia.send_prompt(messages, is_json=False)
        response_text = response.content

        return response_text