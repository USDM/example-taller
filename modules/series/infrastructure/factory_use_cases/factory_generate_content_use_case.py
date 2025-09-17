from ...use_cases.generate_content_use_case.generate_content_use_case import GenerateContentUseCase
from ..generate_content_ia import FactoryGenerateContentIA
from ..last_serie_data import FactoryLastSerie

def create_generate_content_use_case() -> GenerateContentUseCase:
  factory_content_ia = FactoryGenerateContentIA()
  last_Serie_data = FactoryLastSerie()
  return GenerateContentUseCase(
    factory_generate_content_ia=factory_content_ia, 
    factory_last_serie=last_Serie_data)