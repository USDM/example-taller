from . import GeminiIA, ClaudeIA
from modules.series.use_cases.shared import IA
from modules.series.use_cases.dto import IANames
from modules.series.use_cases.dto import UserType
from .chatgpt import ChatGPT

class FactoryIA:

  @staticmethod
  def create(ia_name:IANames) -> IA:
    if ia_name.value == IANames.GEMINI.value:
      return GeminiIA()
    elif ia_name.value == IANames.CLAUDE.value:
      return ClaudeIA()
    else:
      raise ValueError(f"IA name {ia_name} not supported")
    
  @staticmethod
  def create_by_user_type(user_type:UserType) -> list[IA]:
    if user_type.value == UserType.FREE.value:
      return [GeminiIA()]
    elif user_type.value == UserType.SUSCRIBED.value:
      return [GeminiIA(), ClaudeIA()]
    elif user_type.value == UserType.PREMIUM.value:
      return [GeminiIA(), ClaudeIA(), ChatGPT()]
    else:
      raise ValueError(f"User type {user_type} not supported")
    

  @staticmethod
  def create_all() -> list[IA]:
    return [GeminiIA(), ClaudeIA()]