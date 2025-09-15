from ..dto import WindowIndicatorType, WindowIndicatorConfig, UserType
from .interfaces import SeriesRepository, FactoryWindowIndicator
from .errors import InsufficientDataError, UserTypeIndicatorNotAllowedError
"""

Indicatores de ventana:
SMA
ROC
RSI
MACD

"""

class CalculateIndicatorUseCase:

  def __init__(self, series_repository: SeriesRepository, factory_window_indicator: FactoryWindowIndicator):
    self.series_repository = series_repository
    self.factory_window_indicator = factory_window_indicator
    self.subscribed_indicators = [WindowIndicatorType.SMA.value, WindowIndicatorType.ROC.value, WindowIndicatorType.RSI.value]

  def calculate_window_indicator(self, series_id: int, window_indicator_type: WindowIndicatorType, window_indicator_config: WindowIndicatorConfig, user_type: UserType):
    series_data = self.series_repository.get_series_data(series_id)
    if len(series_data) < window_indicator_config.period:
      raise InsufficientDataError(series_id)
    if user_type.value == UserType.FREE.value and window_indicator_type.value != WindowIndicatorType.SMA.value:
      raise UserTypeIndicatorNotAllowedError(user_type.value, window_indicator_type.value)
    if user_type.value == UserType.SUSCRIBED.value and window_indicator_type.value not in self.subscribed_indicators:
      raise UserTypeIndicatorNotAllowedError(user_type.value, window_indicator_type.value)

    window_indicator = self.factory_window_indicator.create_window_indicator(window_indicator_type)
    window_indicator_data = window_indicator.calculate(series_data, window_indicator_config)
    for item in window_indicator_data:
      print(item)
    return window_indicator_data
  