from ...use_cases.dto import LastSerieDataInfo
from modules.common.tables import TableSeriesMatch, TableSeriesData
from ...use_cases.generate_content_use_case.interfaces import LastSerieDataInterface

class LastSerieData(LastSerieDataInterface):
    def get_last_data(self, serie_id:int) -> LastSerieDataInfo:
        name = None
        series = TableSeriesMatch().data
        for serie in series.values():
            if serie.get("id") == serie_id:
                name = serie.get("name")
                break
        data = TableSeriesData().data[serie_id]
        last_data = data[-1]

        return LastSerieDataInfo(
            name = name,
            date = last_data["date"],
            close = last_data["value"]
        )