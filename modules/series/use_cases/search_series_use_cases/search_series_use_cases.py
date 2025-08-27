from .interfaces import FactoryApiSeries
from ..dto import SourceName
from .errors import (
  TokenEmptyError, 
  APINotResponseError, 
  UserTypeNotAllowedError
)
from .interfaces import UserRepository
from modules.common import UserType

"""


free -> series internas 
suscribe, studen -> series en fred o yahoo
pro -> series en fred o yahoo o trading

"""

class SearchSeriesUseCase:

  def __init__(self, factory_api_series:FactoryApiSeries, user_repository:UserRepository):
    self.factory_api_series = factory_api_series
    self.user_repository = user_repository
  
  def search_match_series(self, substring:str, source_name:SourceName, user_id: int):

    try:

      user_basic_info = self.user_repository.get_basic_info(user_id)

      user_type = user_basic_info.user_type
      user_email = user_basic_info.user_email

      if user_type.value == UserType.FREE.value and source_name.value != SourceName.TEST.value:
        raise UserTypeNotAllowedError(user_email, user_type.value, source_name.value)
  
      if (user_type.value == UserType.SUSCRIBED.value or user_type.value == UserType.STUDENT.value) and (source_name.value != SourceName.FRED.value and source_name.value != SourceName.YAHOO.value):
        raise UserTypeNotAllowedError(user_email, user_type.value, source_name.value)
      
      if (user_type.value == UserType.PREMIUM.value) and (source_name.value != SourceName.FRED.value and source_name.value != SourceName.YAHOO.value and source_name.value != SourceName.TRADING.value):
        raise UserTypeNotAllowedError(user_email, user_type.value, source_name.value)  

      api_series = self.factory_api_series.create_api_series(source_name)

      all_series_info = api_series.search_match_series(substring)

      print(f"Searching for series with substring: {substring}")
      for item in all_series_info:
        print(f"Series info: {item}")

    except TokenEmptyError as e:
      print( "almacenar el error en la base de datos" , e)
      #enviar correo
      return
    except APINotResponseError as e:
      print( "api error resposne almacenar el error en la base de datos" , e)
      return
    except Exception as e:
      print( "error inesperado almacenar el error en la base de datos" , e)
      return


