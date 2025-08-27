from ...use_cases.calculate_indicator_use_case.interfaces import SeriesRepository
from ...use_cases.dto import SeriesData
from modules.common.tables import TableSeriesData

class MemorySeriesRepository(SeriesRepository):

  def get_series_data(self, series_id: int) -> list[SeriesData]:
    data = TableSeriesData().data[series_id]
    series_data = [SeriesData(
      date=item["date"], 
      value=item["value"],
      close=item["value"],
      open=item["value"],
      high=item["value"],
      low=item["value"],
      volume=item["value"]
    ) for item in data]
    return series_data