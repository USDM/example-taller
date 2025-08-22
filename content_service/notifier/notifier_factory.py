from .null_email import NullEmail
from .subs_notifier import SubsNotifier
from .notifier import Notifier
from dto import UserType


class NotifierFactory:

  @staticmethod
  def create(user_type:UserType) -> Notifier:
    if user_type.value == UserType.FREE.value:
      return NullEmail()
    elif user_type.value == UserType.SUSCRIBED.value or user_type.value == UserType.PREMIUM.value:
      return SubsNotifier()
    else:
      raise ValueError(f"User type {user_type} not supported")
    

  @staticmethod
  def create_using_plan_config(is_send_email:bool) -> Notifier:
    if is_send_email:
      return SubsNotifier()
    else:
      return NullEmail()