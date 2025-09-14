from ...use_cases.generate_content_use_case.interfaces import SearchUsersInterface
from ....series.use_cases.dto import UserData
from ....common.tables import TableUser

class SearchUsersRepo(SearchUsersInterface):
    def get_users(self) -> list[UserData]:
        users_data = TableUser.data
        all_users = [
            UserData(
                user_email=user["user_email"],
                user_type=user["user_type"]
            )
            for user in users_data.values()
        ]
        return all_users