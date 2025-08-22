from .user_repository import UserRepository
from dto import UserType, PlanConfig
from tables.table_user import TableUser
from tables.table_plan_config import TablePlanConfig

class DataBaseUserRepository(UserRepository):

  def get_user_type(self, user_id:int) -> UserType:
    return TableUser().data[user_id]["user_type"]
  
  def get_user_type_plan_config(self, user_type:UserType) -> PlanConfig:
    return TablePlanConfig().data[user_type]