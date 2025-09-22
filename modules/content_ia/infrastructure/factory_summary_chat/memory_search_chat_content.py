from ...use_cases.summary_use_case.interfaces.i_search_chat_content import ISearchChatContentRepository
from ...use_cases.dto import ChatContent
from ...use_cases.dto import ChatContentResponse
from modules.common.tables import TableChatContentResponse

class MemorySearchChatContent(ISearchChatContentRepository):    
    def get_chat_content(self, chat_content_id: int) -> ChatContent:
        chat_content_response = TableChatContentResponse().data[chat_content_id]

        messages = []
        for message in chat_content_response:
            messages.append(ChatContentResponse(
                id=message["id"],
                questions=message["questions"],
                answers=message["answers"],
            ))

        return ChatContent(
            chat_id=chat_content_id,
            chat_content_response=messages,
        )