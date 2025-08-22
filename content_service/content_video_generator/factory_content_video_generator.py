from . import ProContentVideoGenerator, SuscribeContentVideoGenerator, FreeContentVideoGenerator, BaseContentVideoGenerator
from dto import UserType, SubcontentType

class FactoryContentVideoGenerator:

  @staticmethod
  def create(user_type:UserType) -> BaseContentVideoGenerator:
    if user_type.value == UserType.PREMIUM.value:
      content_video_generator = ProContentVideoGenerator()
    elif user_type.value == UserType.SUSCRIBED.value:
      content_video_generator = SuscribeContentVideoGenerator()
    elif user_type.value == UserType.FREE.value:
      content_video_generator = FreeContentVideoGenerator()
    else:
      raise ValueError(f"User type {user_type} not supported")
    return content_video_generator

