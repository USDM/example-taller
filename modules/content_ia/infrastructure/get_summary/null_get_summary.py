from modules.content_ia.use_cases.summary_use_case.interface.get_summary import GetSummaryInterface
from modules.content_ia.use_cases.shared.base_ia import IA

class NullGetSummary(GetSummaryInterface):
    def get_summary(self, ia: IA, history: list[dict]) -> str:
        return "El usuario no tiene acceso a la funcionalidad de resumen"