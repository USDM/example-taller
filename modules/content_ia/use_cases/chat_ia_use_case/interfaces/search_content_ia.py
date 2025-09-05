from typing import Protocol
from ...dto import Content

class SearchContentIA(Protocol):

    def search(self, content_id: int) -> Content:
        """
        Objetivo: Buscar contenido en base de datos (en memoria)
        """
        pass