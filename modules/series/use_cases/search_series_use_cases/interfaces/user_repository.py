from typing import Protocol
from modules.common import UserType
from dataclasses import dataclass

@dataclass
class UserBasicInfo:
  user_type: UserType
  user_email: str

class UserRepository(Protocol):
  def get_basic_info(self, user_id: int) -> UserBasicInfo:
    pass