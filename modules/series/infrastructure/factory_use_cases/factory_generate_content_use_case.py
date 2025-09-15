from ...use_cases.generate_content_use_case.generate_content_use_case import GenerateContentUseCase
from ..generate_content_ia import GenerateContentIA
from ..last_serie_data import LastSerieData
from ..get_user_data import GetUserData
from ..send_email import SendEmail

def create_generate_content_use_case() -> GenerateContentUseCase:
  generate_content_ia = GenerateContentIA()
  last_Serie_data = LastSerieData()
  get_user_data = GetUserData()
  send_email = SendEmail()
  return GenerateContentUseCase(generate_content_ia, last_Serie_data, get_user_data, send_email)