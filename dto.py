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
  id: int|None = None

  def __str__(self):
    comments_str = '\n    '.join([f"- {comment.text} ({comment.rating.value})" for comment in self.comments])
    questions_str = '\n    '.join([f"- {q}" for q in self.questions])
    answers_str = '\n    '.join([f"- {a}" for a in self.answers])
    topics_str = ', '.join(self.topics)
    
    return f"""
      VideoContent:
        ID: {self.id}
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
  

@dataclass
class SubcontentType(Enum):
  SUMMARY = "summary"
  QUESTION = "question"
  ANSWER = "answer"
  TOPIC = "topic"
  COMMENTS = "comments"
  poema = "poema"


@dataclass
class Error:
  message: str
  title: str
  module: str
  id: int|None = None

  def __str__(self):
    return f"""
      Error:
        ID: {self.id}
        Message: {self.message}
        Title: {self.title}
        Module: {self.module}
      """
