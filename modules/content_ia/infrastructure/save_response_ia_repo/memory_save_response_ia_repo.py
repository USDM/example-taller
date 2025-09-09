from ...use_cases.chat_ia_use_case.interfaces.i_save_response_ia import ISaveResponseIa
from ....common.tables import TableResponseIa

class MemorySaveResponseIaRepo(ISaveResponseIa):
    def save_response(self, message):
        TableResponseIa().data.append(message)
        return TableResponseIa().data