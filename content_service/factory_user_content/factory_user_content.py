from typing import Protocol
from dto import UserType
from ..content_video_generator import ContentVideoGenerator
from ..content_repository import ContentRepository
from ..notifier import Notifier
from ..workflow import Workflow
from utility.ia import IA

class FactoryUserContent(Protocol):

  def create_content_video_generator(self) -> ContentVideoGenerator:
    pass

  def create_content_repository(self) -> ContentRepository:
    pass

  def create_notifier(self) -> Notifier:
    pass

  def create_workflow(self) -> Workflow:
    pass

  def create_all_ias(self) -> list[IA]:
    pass