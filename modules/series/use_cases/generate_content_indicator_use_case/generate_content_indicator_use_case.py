from ..generate_content_use_case.interfaces import LastSerieDataInterface
from ...use_cases.calculate_indicator_use_case.interfaces import SeriesRepository, FactoryWindowIndicator
from ...use_cases.dto import WindowIndicatorType, WindowIndicatorConfig
from .interfaces import IGenerateContentIndicatorIA

class GenerateContentIndicatorUseCase:

    def __init__(self, 
        last_serie_data:LastSerieDataInterface,
        series_repository:SeriesRepository,
        factory_window_indicator:FactoryWindowIndicator,
        i_generate_content_indicator_ia:IGenerateContentIndicatorIA
    ):
        self.last_serie_data = last_serie_data
        self.series_repository = series_repository
        self.factory_window_indicator = factory_window_indicator
        self.i_generate_content_indicator_ia = i_generate_content_indicator_ia
    def generate_content_indicator(self, serie_id:int):
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
        for window_indicator_type in WindowIndicatorType:
            series_data = self.series_repository.get_series_data(serie_id)            
            window_indicator = self.factory_window_indicator.create_window_indicator(window_indicator_type)
            window_indicator_data = window_indicator.calculate(series_data, window_indicator_config)
            ultimo_valor = window_indicator_data[-1]
            indicators_info.append({
                'type': window_indicator_type.name,
                'value': ultimo_valor
            })
        content_indicator_info = self.i_generate_content_indicator_ia.generate_content_indicator_ia(indicators_info, indicators_info)
        return content_indicator_info

