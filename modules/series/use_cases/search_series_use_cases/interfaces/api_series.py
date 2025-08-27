from typing import Protocol
from ...dto import SeriesInfo

class ApiSeries(Protocol):

  def search_match_series(self, substring:str) -> list[SeriesInfo]:
    pass