from ...use_cases.search_series_use_cases.search_series_use_cases import SearchSeriesUseCase
from ...infrastructure.api_series import FactoryApiSeries
from ...infrastructure.user_repository import MemoryUserRepository

def create_series_service() -> SearchSeriesUseCase:
  return SearchSeriesUseCase(
    FactoryApiSeries(),
    MemoryUserRepository()
  )