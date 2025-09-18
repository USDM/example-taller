from ..use_cases.chat_ia_use_case.interfaces import SearchContentRepository
from ..use_cases.dto import Comments
from modules.common.tables import TableResponseIa

class MemorySearchContentFree(SearchContentRepository):
    def get_comments(self, user_id: int) -> Comments:
        comments_db = TableResponseIa().data[user_id]
        content = Comments(
            user_id=user_id,
            comments=comments_db["comments"]
        )
        if len(comments_db["comments"]) > 5 :
            print("El  usuario no puede enviar mas de 5 mensajes")
            return
        print("comments", content.comments)
        return content.comments