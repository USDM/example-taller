from ...use_cases.calculate_indicator_use_case.interfaces import WindowIndicator
from ...use_cases.dto import SeriesData, WindowIndicatorConfig, WindowIndicatorData
import numpy as np

class SMAWindowIndicator(WindowIndicator):

  def calculate(self, series_data: list[SeriesData], window_indicator_config: WindowIndicatorConfig) -> list[WindowIndicatorData]:
    if not series_data or window_indicator_config.period <= 0:
      return []
    
    if len(series_data) < window_indicator_config.period:
      return []
    
    # Extract closing prices from series data
    closing_prices = np.array([data.close for data in series_data])
    
    # Calculate Simple Moving Average using numpy
    sma_values = []
    for i in range(window_indicator_config.period - 1, len(closing_prices)):
      window_start = i - window_indicator_config.period + 1
      window_end = i + 1
      sma_value = np.mean(closing_prices[window_start:window_end])
      sma_values.append(sma_value)
    
    # Create WindowIndicatorData objects with corresponding dates
    result = []
    for i, sma_value in enumerate(sma_values):
      data_index = i + window_indicator_config.period - 1
      result.append(WindowIndicatorData(
        date=series_data[data_index].date,
        value=float(sma_value)
      ))
    
    return result
    