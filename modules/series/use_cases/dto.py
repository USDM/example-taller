from dataclasses import dataclass
from enum import Enum

@dataclass
class SeriesInfo:
  name: str
  description: str
  url: str
  frequency: str

  def __str__(self):
    return f"""
    Name: {self.name}
    Description: {self.description}
    Url: {self.url}
    Frequency: {self.frequency}
    """

@dataclass
class SeriesData:
  date: str
  value: float
  open: float
  high: float
  low: float
  close: float
  volume: float

  def __str__(self):
    return f"""
    Date: {self.date}
    Value: {self.value}
    Open: {self.open}
    High: {self.high}
    Low: {self.low}
    Close: {self.close}
    Volume: {self.volume}
    """

@dataclass
class SourceName(Enum):
  TRADING = "trading"
  YAHOO = "yahoo"
  FRED = "fred"
  TEST = "test"


@dataclass
class WindowIndicatorType(Enum):
  SMA = "sma"
  ROC = "roc"
  RSI = "rsi"
  MACD = "macd"

  def __str__(self):
    return self.value
  

@dataclass
class WindowIndicatorConfig:
  period: int

  def __str__(self):
    return f"""
    Period: {self.period}
    """
  
@dataclass
class WindowIndicatorData:
  date: str
  value: float

  def __str__(self):
    return f"""
    Date: {self.date}
    Value: {self.value}
    """