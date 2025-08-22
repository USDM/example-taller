

from dto import UserType
from . import NullRepository, DatabaseRepository

class FactoryRepository:

  @staticmethod
  def create(user_type:UserType):
    if user_type.value == UserType.FREE.value:
      return NullRepository()
    elif user_type.value == UserType.PREMIUM.value or user_type.value == UserType.SUSCRIBED.value:
      return DatabaseRepository() 
    else:
      raise ValueError(f"User type {user_type} not supported")