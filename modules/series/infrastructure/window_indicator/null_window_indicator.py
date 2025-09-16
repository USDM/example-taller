from ...use_cases.calculate_indicator_use_case.interfaces import WindowIndicator
from ...use_cases.dto import SeriesData, WindowIndicatorConfig, WindowIndicatorData

class NullWindowIndicator(WindowIndicator):

  def calculate(self, series_data: list[SeriesData], window_indicator_config: WindowIndicatorConfig) -> list[WindowIndicatorData]:
    return []