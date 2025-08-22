from .user_repository import UserRepository
from dto import UserType, PlanConfig
from tables.table_user import TableUser
from tables.table_plan_config import TablePlanConfig
from dto import IANames

class MemoryUserRepository(UserRepository):

  def get_user_type(self, user_id:int) -> UserType:
    return UserType(TableUser().data[user_id]["user_type"])
  
  def get_user_type_plan_config(self, user_type:UserType) -> PlanConfig:
    result = TablePlanConfig().data[user_type.value]
    return PlanConfig(
      ia_names=[IANames(ia_name) for ia_name in result["ia_names"]],
      send_email=result["send_email"],
      analyze_apis=result["analyze_apis"]
    )