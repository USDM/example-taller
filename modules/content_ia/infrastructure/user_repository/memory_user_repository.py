from modules.content_ia.use_cases.generate_content_use_case.interfaces import UserRepository
from modules.content_ia.use_cases.dto import UserType, PlanConfig
from modules.common.tables.table_user import TableUser
from modules.common.tables.table_plan_config import TablePlanConfig
from modules.content_ia.use_cases.dto import IANames

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