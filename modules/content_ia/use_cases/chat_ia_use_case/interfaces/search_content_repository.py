from typing import Protocol

from ...dto import Content

class SearchContentRepository(Protocol):
    def get_content(self, content_id: int) -> Content:
        pass