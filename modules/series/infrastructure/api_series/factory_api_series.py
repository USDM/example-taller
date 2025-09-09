from ...use_cases.search_series_use_cases.interfaces import FactoryApiSeries as FactoryApiSeriesInterface
from ...use_cases.dto import SourceName

from .fred_api_series import FredApiSeries
from .test_api_series import TestApiSeries
from .yahoo_api_series import YahooApiSeries
from .google_api_series import GoogleApiSeries

class FactoryApiSeries(FactoryApiSeriesInterface):

  def create_api_series(self, source_name:SourceName):
    if source_name.value == SourceName.TEST.value:
      return TestApiSeries()
    elif source_name.value == SourceName.FRED.value:
      return FredApiSeries()
    elif source_name.value == SourceName.YAHOO.value:
      return YahooApiSeries()
    elif source_name.value == SourceName.GOOGLE.value:
      return GoogleApiSeries()
    else:
      raise ValueError(f"Source name {source_name} not supported")