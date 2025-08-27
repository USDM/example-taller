from ...use_cases.calculate_indicator_use_case.interfaces import WindowIndicator
from ...use_cases.dto import SeriesData, WindowIndicatorConfig, WindowIndicatorData
import numpy as np

class ROCWindowIndicator(WindowIndicator):

  def calculate(self, series_data: list[SeriesData], window_indicator_config: WindowIndicatorConfig) -> list[WindowIndicatorData]:
    if not series_data or window_indicator_config.period <= 0:
      return []
    
    if len(series_data) < window_indicator_config.period + 1:
      return []
    
    # Extract closing prices from series data
    closing_prices = np.array([data.close for data in series_data])
    
    # Calculate Rate of Change using numpy
    # ROC = ((current_price - price_n_periods_ago) / price_n_periods_ago) * 100
    roc_values = []
    for i in range(window_indicator_config.period, len(closing_prices)):
      current_price = closing_prices[i]
      price_n_periods_ago = closing_prices[i - window_indicator_config.period]
      
      if price_n_periods_ago != 0:  # Avoid division by zero
        roc_value = ((current_price - price_n_periods_ago) / price_n_periods_ago) * 100
        roc_values.append(roc_value)
      else:
        roc_values.append(0.0)  # Return 0 if previous price is 0
    
    # Create WindowIndicatorData objects with corresponding dates
    result = []
    for i, roc_value in enumerate(roc_values):
      data_index = i + window_indicator_config.period
      result.append(WindowIndicatorData(
        date=series_data[data_index].date,
        value=float(roc_value)
      ))
    
    return result