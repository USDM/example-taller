from ...use_cases.chat_ia_use_case.interfaces.search_content_ia import SearchContentIA
from ...use_cases.dto import Content, ContentComment, ContentCommentRating, ContentMetadata
from ....common.tables.table_content_ia import TableContentIA

class SearchContentRepository(SearchContentIA):

    def search(self, content_id: int) -> Content:
        content = TableContentIA().data[content_id]
        print(content)
        return Content(
            text=content["text"],
            metadata=ContentMetadata(
                title=content["metadata"]["title"],
                authors=content["metadata"]["authors"]
            ),
            comments=[ContentComment(
                text=comment["comment"],
                rating=ContentCommentRating(comment["rating"]),
                reasoning=comment["reasoning"]
            ) for comment in content["comments"]],
            summary=content["summary"],
            questions=content["questions"],
            answers=content["answers"],
            topics=content["topics"],
            ia_name=content["ia_name"],
            critical_perspective=content["critical_perspective"],
            sources=content["sources"],
            id=content_id
        )