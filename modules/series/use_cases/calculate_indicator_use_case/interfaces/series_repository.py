from typing import Protocol
from ...dto import SeriesData

class SeriesRepository(Protocol):

  def get_series_data(self, series_id: int) -> list[SeriesData]:
    pass