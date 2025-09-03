from typing import Protocol
from modules.content_ia.use_cases.dto import Content

"""
    Objetivo: Buscar contenido
    Solo va a cambiar cuando la lógica de busqueda de contenido cambie
"""
class SearchContentRepository(Protocol):
    def search_content(self, content_id: int) -> Content:
        pass