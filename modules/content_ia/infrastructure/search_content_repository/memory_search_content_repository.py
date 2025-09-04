from ...use_cases.chat_ia_use_case.interfaces import SearchContentRepository
from ....common.tables import TableContent
from ...use_cases.dto import Content

class MemorySearchContentRepository(SearchContentRepository):
  
  def get_content(self, content_id:int):
    content_db = TableContent().data[content_id]
    content = Content(
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
      id=content_id
    )
    return content