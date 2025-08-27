from ...use_cases.calculate_indicator_use_case.calculate_indicator_use_case import CalculateIndicatorUseCase
from ..series_repository import MemorySeriesRepository
from ..window_indicator import FactoryWindowIndicator

def create_calculate_indicator_use_case() -> CalculateIndicatorUseCase:
  series_repository = MemorySeriesRepository()
  factory_window_indicator = FactoryWindowIndicator()
  return CalculateIndicatorUseCase(series_repository, factory_window_indicator)