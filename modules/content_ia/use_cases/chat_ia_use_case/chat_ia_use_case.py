from .interfaces.search_content_ia import SearchContentIA
from ...use_cases.shared.base_ia import IA

class ChatIAUseCase:

    def __init__(self, search_content_ia: SearchContentIA, base_ia: IA):
        self.search_content_ia = search_content_ia
        self.base_ia = base_ia

    def chat_ia(self, content_id: int, message: str) -> str:

        """
        Objetivo: 
        - Generar un chat con ia para contenido
        Intrucciones:
        1.-Recibir id de contenido y el mensaje del usuario
        2.- Obtener el contenido
        3.- Generar un chat con ia para contenido
        4.- Retornar la respuesta del chat

        1.- none
        2.- chat_ia_repository
        3.- base_ia
        4.- none
        """

        content = self.search_content_ia.search(content_id)
        return self.base_ia.chat(content, message)

        