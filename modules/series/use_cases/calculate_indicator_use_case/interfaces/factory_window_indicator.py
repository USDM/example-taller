from typing import Protocol
from ...dto import WindowIndicatorType
from .window_indicator import WindowIndicator

class FactoryWindowIndicator(Protocol):

  def create_window_indicator(self, window_indicator_type: WindowIndicatorType) -> WindowIndicator:
    pass