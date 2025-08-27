from ...use_cases.search_series_use_cases.interfaces import ApiSeries
from ...use_cases.dto import SeriesInfo
from ...use_cases.search_series_use_cases.errors import APINotResponseError

class FredApiSeries(ApiSeries):

  def search_match_series(self, substring:str) -> list[SeriesInfo]:

    """
    LOGICA DE QUE FRED NO ME RESPONDE
    """

    raise APINotResponseError("fred")

    print(f"Searching for series with substring: {substring} in FredApiSeries")
    return []