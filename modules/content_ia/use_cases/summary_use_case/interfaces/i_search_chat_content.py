from typing import Protocol
from ...dto import ChatContent


class ISearchChatContentRepository(Protocol):
    def get_chat_content(self, chat_content_id: int) -> ChatContent:
        pass



