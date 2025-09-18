from ...dto import UserType
from typing import Protocol
from .search_comments_repository import SearchCommentsRepository

class FactoryUserComments(Protocol):
    def create_user_comments(self, user_type: UserType) ->  SearchCommentsRepository:
        pass