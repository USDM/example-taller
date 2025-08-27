from ...use_cases.search_series_use_cases.interfaces import UserRepository
from modules.common import UserType
from modules.common.tables import TableUser
from ...use_cases.search_series_use_cases.interfaces.user_repository import UserBasicInfo

class MemoryUserRepository(UserRepository):
  def get_basic_info(self, user_id: int) -> UserBasicInfo:
    data = TableUser().data
    user_basic_info = data[user_id]
    return UserBasicInfo(
      user_type=UserType(user_basic_info["user_type"]),
      user_email=user_basic_info["user_email"]
    )