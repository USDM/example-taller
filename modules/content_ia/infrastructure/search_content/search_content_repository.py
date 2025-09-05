from modules.content_ia.use_cases.dto import Content, ContentMetadata, ContentComment, ContentCommentRating
from modules.content_ia.use_cases.chat_ia_use_case.interfaces.search_content import SearchContent
from modules.common.tables.table_content import TableContent

class SearchContentRepository(SearchContent):

    def search(self, content_id: int) -> Content:
        result = TableContent().data[content_id]
        return Content(
            text=result["text"],
            metadata=ContentMetadata(
                title=result["metadata"]["title"],
                authors=result["metadata"]["authors"]
            ),
            comments=[ContentComment(
                text=comment["text"],
                rating=ContentCommentRating(comment["rating"]),
                reasoning=comment["reasoning"]
            ) for comment in result["comments"]],
            summary=result["summary"],
            questions=result["questions"],
            answers=result["answers"],
            topics=result["topics"],
            ia_name=result["ia_name"],
            critical_perspective=result["critical_perspective"],
            sources=result["sources"],
            id=content_id
        )