from ...use_cases.generate_content_indicator_use_case import GenerateContentIndicatorUseCase
from ..last_serie_data import LastSerieData
from ..series_repository import MemorySeriesRepository
from ..window_indicator import FactoryWindowIndicator
from ..generate_content_indicator_ia import GenerateContentIndicatorIA
from ..get_prompt import GetPromptFactory

def create_generate_content_indicator_use_case() -> GenerateContentIndicatorUseCase:
    last_serie_data = LastSerieData()
    series_repository = MemorySeriesRepository()
    factory_window_indicator = FactoryWindowIndicator()
    i_generate_content_indicator_ia = GenerateContentIndicatorIA()
    get_prompt_factory = GetPromptFactory()
    return GenerateContentIndicatorUseCase(last_serie_data, series_repository, factory_window_indicator, i_generate_content_indicator_ia, get_prompt_factory)
