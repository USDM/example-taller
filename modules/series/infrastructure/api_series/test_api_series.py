from ...use_cases.search_series_use_cases.interfaces import ApiSeries
from ...use_cases.dto import SeriesInfo
from ....common.tables import TableSeriesMatch

class TestApiSeries(ApiSeries):

  def search_match_series(self, substring:str) -> list[SeriesInfo]:
    data = TableSeriesMatch().data
    return [SeriesInfo(**data[key]) for key in data if substring in key]