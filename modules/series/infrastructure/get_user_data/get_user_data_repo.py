from ...use_cases.generate_content_use_case.interfaces import GetUserDataInterface
from modules.common import UserType
from modules.common.tables import TableUser
from ...use_cases.dto import User

class GetUserData(GetUserDataInterface):
    def get_user(self, user_id: int) -> User:
        data = TableUser().data
        user_basic_info = data[user_id]
        return User(
            user_type=UserType(user_basic_info["user_type"]),
            email=user_basic_info["user_email"]
        )