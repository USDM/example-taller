from ...use_cases.search_series_use_cases.interfaces import ApiSeries
from ...use_cases.dto import SeriesInfo

class YahooApiSeries(ApiSeries):

  def search_match_series(self, substring:str) -> list[SeriesInfo]:
    print(f"Searching for series with substring: {substring} in YahooApiSeries")
    return []