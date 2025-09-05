from modules.content_ia.use_cases.dto import Content
from typing import Protocol

class SearchContent(Protocol):

    def search(self, content_id: int) -> Content:
        pass