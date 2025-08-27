from abc import ABC, abstractmethod
from modules.content_ia.use_cases.shared import IA
from dataclasses import dataclass
from .base_content_video_generator import BaseContentVideoGenerator
from .content_repository import ContentRepository
from .notifier import Notifier
from .workflow import Workflow

@dataclass
class UserContentPlanConfig:
  workflow: Workflow
  notifier: Notifier
  ias: list[IA]

class FactoryUserContent(ABC):

  @abstractmethod
  def create_content_video_generator(self) -> BaseContentVideoGenerator:
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