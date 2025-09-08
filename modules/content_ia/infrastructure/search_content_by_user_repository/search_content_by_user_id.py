from ...use_cases.emails_use_case.interfaces.search_content_by_user_repository import SearchContentByUserRepository
from ...use_cases.dto import Content
from ....common.tables.table_user_content import TableUserContent
from ....common.tables.table_user import TableUser

class SearchContentByUserId(SearchContentByUserRepository):    
    def get_content_by_user_id(self, user_id: int) -> list[Content]:
        all_contents = []
        contents = TableUserContent().data[user_id]
        for content_db in contents:
            all_contents.append(Content(
            text=content_db["text"],
            metadata=content_db["metadata"],
            comments=content_db["comments"],
            summary=content_db["summary"],
            questions=content_db["questions"],
            answers=content_db["answers"],
            topics=content_db["topics"],
            ia_name=content_db["ia_name"],
            critical_perspective=content_db["critical_perspective"],
            sources=content_db["sources"],
            ))

        return all_contents
        
    def get_user_email(self, user_id: int) -> str:
        user = TableUser().data[user_id]
        return user["user_email"]