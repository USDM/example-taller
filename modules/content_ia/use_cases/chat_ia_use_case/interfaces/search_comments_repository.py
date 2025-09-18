from typing import Protocol

from ...dto import Comments

class SearchCommentsRepository(Protocol):
    def get_comments(self, user_id: int) -> Comments:
        pass