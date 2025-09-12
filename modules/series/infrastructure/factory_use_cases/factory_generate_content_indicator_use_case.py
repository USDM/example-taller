from ...use_cases.generate_content_indicator_use_case import GenerateContentIndicatorUseCase
from ..last_serie_data import LastSerieData
from ..series_repository import MemorySeriesRepository
from ..window_indicator import FactoryWindowIndicator

def create_generate_content_indicator_use_case() -> GenerateContentIndicatorUseCase:
    last_serie_data = LastSerieData()
    series_repository = MemorySeriesRepository()
    factory_window_indicator = FactoryWindowIndicator()
    return GenerateContentIndicatorUseCase(last_serie_data, series_repository, factory_window_indicator)
