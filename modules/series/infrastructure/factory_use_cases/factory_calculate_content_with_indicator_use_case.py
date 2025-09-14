from modules.series.use_cases.generate_content_use_case.interfaces.search_users_interface import SearchUsersInterface
from ...use_cases.generate_content_use_case.generate_content_use_case import GenerateContentUseCase
from ..generate_content_ia import GenerateContentIA
from ..last_serie_data import LastSerieData
from ..series_repository import MemorySeriesRepository
from ..window_indicator import FactoryWindowIndicator
from..search_users_repo import SearchUsersRepo
from ..send_email_repository import SendEmailRepository

def create_generate_content_with_indicator_use_case() -> GenerateContentUseCase:
  generate_content_ia = GenerateContentIA()
  last_serie_data = LastSerieData()
  serie_data = MemorySeriesRepository()
  factory_indicator = FactoryWindowIndicator()
  users = SearchUsersRepo()
  send_email = SendEmailRepository()
  return GenerateContentUseCase(
        generate_content_ia=generate_content_ia, 
        last_serie_data=last_serie_data,
        factory_window_inidicator=factory_indicator,
        serie_data=serie_data,
        users= users,
        send_email=send_email
    )