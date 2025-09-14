from ...use_cases.generate_content_use_case.generate_content_use_case import GenerateContentUseCase
from ..generate_content_ia import GenerateContentIA
from ..last_serie_data import LastSerieData
from ..series_repository import MemorySeriesRepository
from ..window_indicator import FactoryWindowIndicator

def create_generate_content_with_indicator_use_case() -> GenerateContentUseCase:
  generate_content_ia = GenerateContentIA()
  last_serie_data = LastSerieData()
  serie_data = MemorySeriesRepository()
  factory_indicator = FactoryWindowIndicator()
  return GenerateContentUseCase(
        generate_content_ia=generate_content_ia, 
        last_serie_data=last_serie_data,
        factory_window_inidicator=factory_indicator,
        serie_data=serie_data
    )