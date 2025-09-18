from ...dto import UserType
from typing import Protocol
from .resume_comments_repository import ResumeCommentsRepository

class FactoryResumeComments(Protocol):
    def create_resume_comments(self, user_type: UserType) -> ResumeCommentsRepository:
        pass