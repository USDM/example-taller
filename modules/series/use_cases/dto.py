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
class LastSerieDataInfo:
  name: str
  date: str
  close: float

  def __str__(self):
    return f"""
    Name: {self.name}
    Date: {self.date}
    Close: {self.close}
    """

@dataclass
class ContentSerie:
  comments: list[str]
  summary: str
  projections: str

  def __str__(self):
    comments_str = ', '.join(self.comments)

    return f"""
    Comments:
      {self.comments}

    Summary:
      {self.summary}

    Projections:
      {self.projections}
    """

@dataclass
class SourceName(Enum):
  TRADING = "trading"
  YAHOO = "yahoo"
  FRED = "fred"
  TEST = "test"
  GOOGLE = "google"


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

@dataclass
class IANames(Enum):
  CLAUDE = "claude"
  GEMINI = "gemini"

@dataclass
class UserType(Enum):
  FREE = "free"
  SUSCRIBED = "subscribed"
  PREMIUM = "premium"
  STUDENT = "student"