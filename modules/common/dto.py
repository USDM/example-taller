from dataclasses import dataclass
from enum import Enum


@dataclass
class UserType(Enum):
  FREE = "free"
  SUSCRIBED = "subscribed"
  PREMIUM = "premium"
  STUDENT = "student"