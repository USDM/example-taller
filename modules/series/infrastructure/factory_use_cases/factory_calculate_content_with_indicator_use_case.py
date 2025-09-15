from modules.series.use_cases.generate_content_use_case.interfaces.search_users_interface import SearchUsersInterface
from ...use_cases.generate_content_use_case.generate_content_use_case import GenerateContentUseCase
from ..generate_content_ia import FactoryGenerateContentIA
from ..last_serie_data import LastSerieData
from ..series_repository import MemorySeriesRepository
from ..window_indicator import FactoryWindowIndicator
from..search_users_repo import SearchUsersRepo
from ..send_email_repository import SendEmailRepository
from ..validate_user_repo import ValidateUserRepo

def create_generate_content_with_indicator_use_case() -> GenerateContentUseCase:
  last_serie_data = LastSerieData()
  serie_data = MemorySeriesRepository()
  factory_indicator = FactoryWindowIndicator()
  users = SearchUsersRepo()
  send_email = SendEmailRepository()
  validate_user = ValidateUserRepo()
  factory_content_ia = FactoryGenerateContentIA()
  return GenerateContentUseCase(
        last_serie_data=last_serie_data,
        factory_window_inidicator=factory_indicator,
        serie_data=serie_data,
        users= users,
        send_email=send_email,
        validate_user=validate_user,
        factory_generate_content_ia=factory_content_ia
    )