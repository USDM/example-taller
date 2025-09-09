from ...use_cases.calculate_indicator_use_case.interfaces import FactoryWindowIndicator as FactoryWindowIndicatorInterface, WindowIndicator
from ...use_cases.dto import WindowIndicatorType
from .sma_window_indicator import SMAWindowIndicator
from .roc_window_indicator import ROCWindowIndicator
from .rsi_window_indicator import RSIWindowIndicator
from .macd_window_indicator import MACDWindowIndicator

class FactoryWindowIndicator(FactoryWindowIndicatorInterface):

  def create_window_indicator(self, window_indicator_type: WindowIndicatorType) -> WindowIndicator:
    if window_indicator_type.value == WindowIndicatorType.SMA.value:
      return SMAWindowIndicator()
    elif window_indicator_type.value == WindowIndicatorType.ROC.value:
      return ROCWindowIndicator()
    elif window_indicator_type.value == WindowIndicatorType.RSI.value:
      return RSIWindowIndicator()
    elif  window_indicator_type.value == WindowIndicatorType.MACD.value:
      return MACDWindowIndicator()
    else:
      raise ValueError(f"Window indicator type {window_indicator_type} not supported")