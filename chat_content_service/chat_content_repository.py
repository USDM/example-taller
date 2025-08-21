from dto import VideoContent, VideoMetadata

class ChatContentRepository:

  def get_video_content(self, video_content_id:int) -> VideoContent:
    return VideoContent(
      text="",
      metadata=VideoMetadata(
        title="",
        authors=[]
      ),
      comments=[],
      summary="Temas economicos, politicos, sociales, etc.",
      questions=[],
      answers=[],
      topics=[]
    )