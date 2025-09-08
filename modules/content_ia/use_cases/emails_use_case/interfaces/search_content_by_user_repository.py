from typing import Protocol
from ...dto import Content

class SearchContentByUserRepository(Protocol):

    def get_content_by_user_id(self, user_id: int) -> list[Content]:
        pass

    def get_user_email(self, user_id: int) -> str:
        pass