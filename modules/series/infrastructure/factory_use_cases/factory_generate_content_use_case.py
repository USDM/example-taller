from ...use_cases.generate_content_use_case.generate_content_use_case import GenerateContentUseCase
from ..generate_content_ia import GenerateContentIA
from ..last_serie_data import LastSerieData

def create_generate_content_use_case() -> GenerateContentUseCase:
  generate_content_ia = GenerateContentIA()
  last_Serie_data = LastSerieData()
  return GenerateContentUseCase(generate_content_ia, last_Serie_data)