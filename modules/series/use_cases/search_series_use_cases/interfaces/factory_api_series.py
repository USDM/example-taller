from typing import Protocol
from .api_series import ApiSeries
from ...dto import SourceName

class FactoryApiSeries(Protocol):

  def create_api_series(self, source_name:SourceName) -> ApiSeries:
    pass