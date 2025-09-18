from ...use_cases.dto import UserType
from ...use_cases.chat_ia_use_case.interfaces import ResumeCommentsRepository, FactoryResumeComments
from .resume_comment_free import ResumeCommentsFree
from .resume_comment_repository import ResumeCommentRepository
from .resume_comment_suscribed import ResumeCommentsSuscribed

class FactoryResumeComments(FactoryResumeComments):
    def create_resume_comments(self, user_type: UserType) -> ResumeCommentsRepository:
        if user_type.value == UserType.PREMIUM.value or user_type.value== UserType.STUDENT.value:
            return ResumeCommentRepository()
        elif user_type.value == UserType.FREE.value:
            return ResumeCommentsFree()
        elif user_type.value == UserType.SUSCRIBED.value:
            return ResumeCommentsSuscribed()
        else:
            raise("Tipo se usuario no soportado")