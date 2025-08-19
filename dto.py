from dataclasses import dataclass
from enum import Enum

@dataclass
class VideoMetadata:
  title: str
  authors: list[str]

@dataclass
class VideoCommentRating(Enum):
  POSITIVE = "positive"
  NEGATIVE = "negative"
  NEUTRAL = "neutral"

  def __str__(self):
    return f"{self.value}"

@dataclass
class VideoComment:
  text: str
  rating: VideoCommentRating
  reasoning: str

@dataclass
class VideoContent:
  text: str
  metadata: VideoMetadata
  comments: list[VideoComment]
  summary: str
  questions: list[str]
  answers: list[str]
  topics: list[str]

  def __str__(self):
    comments_str = '\n    '.join([f"- {comment.text} ({comment.rating.value})" for comment in self.comments])
    questions_str = '\n    '.join([f"- {q}" for q in self.questions])
    answers_str = '\n    '.join([f"- {a}" for a in self.answers])
    topics_str = ', '.join(self.topics)
    
    return f"""
      VideoContent:
        Title: {self.metadata.title}
        Authors: {', '.join(self.metadata.authors)}
        
        Summary:
          {self.summary}
        
        Topics: {topics_str}
        
        Questions:
          {questions_str}
        
        Answers:
          {answers_str}
        
        Comments:
          {comments_str}
      """