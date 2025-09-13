from typing import Protocol
from ...dto import SeriesData, WindowIndicatorConfig, WindowIndicatorData

class WindowIndicator(Protocol):

  def calculate(self, series_data: list[SeriesData], window_indicator_config: WindowIndicatorConfig) -> list[WindowIndicatorData]:
    pass