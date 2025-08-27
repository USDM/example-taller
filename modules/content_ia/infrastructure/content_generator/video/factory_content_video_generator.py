from . import ProContentVideoGenerator, SuscribeContentVideoGenerator, FreeContentVideoGenerator
from modules.content_ia.use_cases.generate_content_use_case.interfaces import BaseContentGenerator
from modules.content_ia.use_cases.dto import UserType

class FactoryContentVideoGenerator:

  @staticmethod
  def create(user_type:UserType) -> BaseContentGenerator:
    if user_type.value == UserType.PREMIUM.value:
      content_video_generator = ProContentVideoGenerator()
    elif user_type.value == UserType.SUSCRIBED.value:
      content_video_generator = SuscribeContentVideoGenerator()
    elif user_type.value == UserType.FREE.value:
      content_video_generator = FreeContentVideoGenerator()
    else:
      raise ValueError(f"User type {user_type} not supported")
    return content_video_generator

