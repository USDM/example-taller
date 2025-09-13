from modules.series.use_cases.generate_content_use_case.interfaces import generate_content_ia_interface, last_serie_data_interface
from .interfaces import (
    GenerateContentIAInterface,
    LastSerieDataInterface,
    FactoryWindowIndicator,
    LastIndicatorDataInterface
)

from ..dto import WindowIndicatorType, WindowIndicatorConfig

class GenerateContentUseCase:

    def __init__(self, 
            generate_content_ia:GenerateContentIAInterface, 
            last_serie_data:LastSerieDataInterface,
            factory_window_inidicator: FactoryWindowIndicator,
            last_inidicator_data: LastIndicatorDataInterface
            ):
        self.generate_content_ia = generate_content_ia
        self.last_serie_data = last_serie_data
        self.window_indicator = factory_window_inidicator
        self.last_indicator_data = last_inidicator_data

    def generate_content_serie(self, serie_id:int):
        """
        1. Obtener el nombre y ultimo dato de la serie
        2. Obtener el prompt
        3. Enviar datos a la IA (Generar contenido)
        4. recibir respuesta

        1. last_serie_data_interface
        2. search_prompt_interface
        3. generate_content_ia_interface
        4. None
        """

        serie_info = self.last_serie_data.get_last_data(serie_id)
        content_serie = self.generate_content_ia.generate_content(serie_info)

        return content_serie

    def generate_content_serie_with_inidicators(self, serie_id:int):
        """
        1. Obtener el nombre y ultimo dato de la serie
        2. Calcular cada indicador
        3. Obtener ultimo dato de cada calculo del inidicador
        4. Por cada inidicador mandar el ultimo dato de la seria, nombre y el indicador correspondiente al prompt

        1. last_serie_data_interface
        2. factory_window_inidicator (necesita window_indicator)
        3. last_indicator_data
        4. generate_content_ia_interface
        """
        serie_info = self.last_serie_data.get_last_data(serie_id)
        for indicator in WindowIndicatorType.values():
            window_indicator = self.window_indicator.create_window_indicator(
                                                        window_indicator_type=WindowIndicatorType
                                                        )
            calculate_indicator = window_indicator.calculate(
                series_data=serie_info,
                window_indicator_config=WindowIndicatorConfig(period=2)
            )
            last_indicator_data = self.last_indicator_data.get_last_indicator_data(
                indicator_data= calculate_indicator
            )
            content_serie = self.generate_content_ia.generate_content_with_indicator(
                serie_info=serie_info,
                last_indicator_data = last_indicator_data,
                type_indicator=indicator
            )





            

