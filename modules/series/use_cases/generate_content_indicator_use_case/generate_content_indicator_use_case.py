from ..generate_content_use_case.interfaces import LastSerieDataInterface
from ...use_cases.calculate_indicator_use_case.interfaces import SeriesRepository, FactoryWindowIndicator
from ...use_cases.dto import WindowIndicatorType, WindowIndicatorConfig, UserType
from .interfaces import IGenerateContentIndicatorIA, ValidateSerieUserTypeInterface
from ...infrastructure.get_prompt import GetPromptFactory
from ...infrastructure.send_email import SendEmailFactory

class GenerateContentIndicatorUseCase:

    def __init__(self, 
        last_serie_data:LastSerieDataInterface,
        series_repository:SeriesRepository,
        factory_window_indicator:FactoryWindowIndicator,
        i_generate_content_indicator_ia:IGenerateContentIndicatorIA,
        get_prompt_factory:GetPromptFactory,
        send_email_factory:SendEmailFactory,
        validate_serie_user_type:ValidateSerieUserTypeInterface
    ):
        self.last_serie_data = last_serie_data
        self.series_repository = series_repository
        self.factory_window_indicator = factory_window_indicator
        self.i_generate_content_indicator_ia = i_generate_content_indicator_ia
        self.get_prompt_factory = get_prompt_factory
        self.send_email_factory = send_email_factory
        self.validate_serie_user_type = validate_serie_user_type
    def generate_content_indicator(self, serie_id:int, user_type:UserType):
        """
        1.-Recibir serie_id
        2.-Obtener el ultimo dato de la serie
        3.-Obtener el nombre de la serie
        4.-Obtener los ultimos datos de cada uno de los indicadores que tenemos
        5.-Generar el contenido

        1.- None
        2.- LastSerieDataInterface
        3.- None
        4.- None
        5.- generate_content_indicator_ia_interface
        """
        serie_info = self.last_serie_data.get_last_data(serie_id)
        window_indicator_config = WindowIndicatorConfig(period=2)
        indicators_info = []

        if not self.validate_serie_user_type.validate_user_type(serie_id, user_type):
            return None, "Serie not allowed for user type"

        series_data = self.series_repository.get_series_data(serie_id)

        for window_indicator_type in WindowIndicatorType:
            window_indicator = self.factory_window_indicator.create_window_indicator_with_user_type(window_indicator_type, user_type)
            window_indicator_data = window_indicator.calculate(series_data, window_indicator_config)
            if len(window_indicator_data) > 0:
                ultimo_valor = window_indicator_data[-1]
                indicators_info.append({
                    'type': window_indicator_type.name,
                    'value': ultimo_valor
                })

        prompt_getter = self.get_prompt_factory.create(user_type)
        prompt = prompt_getter.get_prompt(serie_info, indicators_info)

        content_indicator_info = self.i_generate_content_indicator_ia.generate_content_indicator_ia(prompt)

        email_sender = self.send_email_factory.create(user_type)
        message = email_sender.send_email(user_type)

        return content_indicator_info, message

