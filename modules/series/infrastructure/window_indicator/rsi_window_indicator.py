from ...use_cases.calculate_indicator_use_case.interfaces import WindowIndicator
from ...use_cases.dto import SeriesData, WindowIndicatorConfig, WindowIndicatorData
import numpy as np

class RSIWindowIndicator(WindowIndicator):

  def calculate(self, series_data: list[SeriesData], window_indicator_config: WindowIndicatorConfig) -> list[WindowIndicatorData]:
    if not series_data or window_indicator_config.period <= 0:
      return []
    
    if len(series_data) < window_indicator_config.period + 1:
      return []
    
    # Extract closing prices from series data
    closing_prices = np.array([data.close for data in series_data])
    
    # Calculate price changes (deltas)
    price_deltas = np.diff(closing_prices)
    
    # Separate gains and losses
    gains = np.where(price_deltas > 0, price_deltas, 0)
    losses = np.where(price_deltas < 0, -price_deltas, 0)
    
    # Calculate RSI values
    rsi_values = []
    period = window_indicator_config.period
    
    for i in range(period - 1, len(gains)):
      # Get the window of gains and losses
      window_start = i - period + 1
      window_end = i + 1
      
      window_gains = gains[window_start:window_end]
      window_losses = losses[window_start:window_end]
      
      # Calculate average gain and loss
      avg_gain = np.mean(window_gains)
      avg_loss = np.mean(window_losses)
      
      # Calculate RSI
      if avg_loss == 0:
        # If there are no losses, RSI = 100
        rsi_value = 100.0
      else:
        rs = avg_gain / avg_loss
        rsi_value = 100 - (100 / (1 + rs))
      
      rsi_values.append(rsi_value)
    
    # Create WindowIndicatorData objects with corresponding dates
    result = []
    for i, rsi_value in enumerate(rsi_values):
      # The RSI starts at index period (because we need period+1 data points for period deltas)
      data_index = i + period
      result.append(WindowIndicatorData(
        date=series_data[data_index].date,
        value=float(rsi_value)
      ))
    
    return result
    