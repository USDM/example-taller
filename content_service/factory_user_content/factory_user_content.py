from abc import ABC, abstractmethod
from dto import UserType
from ..content_video_generator import ContentVideoGenerator
from ..content_repository import ContentRepository
from ..notifier import Notifier, NullEmail, SubsNotifier, NotifierFactory
from ..workflow import Workflow, NullWorkflow, SubsWorkFlow, FactoryWorkflow
from utility.ia import IA, FactoryIA
from dto import PlanConfig
from dataclasses import dataclass

@dataclass
class UserContentPlanConfig:
  workflow: Workflow
  notifier: Notifier
  ias: list[IA]

class FactoryUserContent(ABC):

  @abstractmethod
  def create_content_video_generator(self) -> ContentVideoGenerator:
    pass
  
  @abstractmethod
  def create_content_repository(self) -> ContentRepository:
    pass

  @abstractmethod
  def create_notifier(self) -> Notifier:
    pass

  @abstractmethod
  def create_workflow(self) -> Workflow:
    pass
  
  @abstractmethod
  def create_all_ias(self) -> list[IA]:
    pass

  def create_using_plan_config(self, plan_config:PlanConfig) -> UserContentPlanConfig:
    workflow = FactoryWorkflow.create_using_plan_config(plan_config.analyze_apis)
    notifier = NotifierFactory.create_using_plan_config(plan_config.send_email)
    ias = [ FactoryIA.create(ia_name) for ia_name in plan_config.ia_names ]
    return UserContentPlanConfig(
      workflow=workflow,
      notifier=notifier,
      ias=ias
    )