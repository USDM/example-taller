from typing import Protocol
from modules.content_ia.use_cases.dto import PlanConfig
from modules.content_ia.use_cases.dto import UserType

class UserRepository(Protocol):
  
  def get_user_type(self, user_id:int) -> UserType:
    pass
  
  def get_user_type_plan_config(self, user_type:UserType) -> PlanConfig:
    pass