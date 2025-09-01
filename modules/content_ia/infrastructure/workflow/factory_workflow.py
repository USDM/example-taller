from .null_workflow import NullWorkflow
from .subs_work_flow import SubsWorkFlow
from modules.content_ia.use_cases.dto import UserType
from modules.content_ia.use_cases.generate_content_use_case.interfaces import Workflow

class FactoryWorkflow:

  @staticmethod
  def create(user_type:UserType) -> Workflow:
    if user_type.value == UserType.FREE.value:
      return NullWorkflow()
    elif user_type.value == UserType.PREMIUM.value or user_type.value == UserType.SUSCRIBED.value:
      return SubsWorkFlow()
    
  @staticmethod
  def create_using_plan_config(analyze_apis:bool) -> Workflow:
    if analyze_apis:
      return SubsWorkFlow()
    else:
      return NullWorkflow()