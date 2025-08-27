from modules.content_ia.use_cases.generate_content_use_case.interfaces import UserRepository
from modules.content_ia.use_cases.dto import UserType, PlanConfig
from modules.common.tables.table_user import TableUser
from modules.common.tables.table_plan_config import TablePlanConfig

class DataBaseUserRepository(UserRepository):

  def get_user_type(self, user_id:int) -> UserType:
    return TableUser().data[user_id]["user_type"]
  
  def get_user_type_plan_config(self, user_type:UserType) -> PlanConfig:
    return TablePlanConfig().data[user_type]