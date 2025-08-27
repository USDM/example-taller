from abc import ABC, abstractmethod
from modules.content_ia.use_cases.shared import IA
from dataclasses import dataclass
from .base_content_generator import BaseContentGenerator
from .content_repository import ContentRepository
from .notifier import Notifier
from .workflow import Workflow
from modules.content_ia.use_cases.dto import SourceType

@dataclass
class UserContentPlanConfig:
  workflow: Workflow
  notifier: Notifier
  ias: list[IA]

class FactoryUserContent(ABC):

  @abstractmethod
  def create_content_generator(self, source_type:SourceType) -> BaseContentGenerator:
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

  @abstractmethod
  def create_using_plan_config(self, plan_config: UserContentPlanConfig) -> UserContentPlanConfig:
    pass