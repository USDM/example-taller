from ...use_cases.chat_with_content_use_case.interfaces import SearchContentRepository as SearchContentRepositoryInterface
from ...use_cases.dto import Content
from modules.common.tables.table_content import TableContent

class SearchContentRepository(SearchContentRepositoryInterface):
    def search_content(self, content_id: int) -> Content:
        return TableContent().data[content_id]