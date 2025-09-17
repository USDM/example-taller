from typing import Optional

from .interfaces import (
    LastSerieDataInterface,
    FactoryWindowIndicator,
    SeriesRepository,
    SearchUsersInterface,
    FactoryGenerateContentIA,
    FactoryValidateUser,
    FactorySendEmail,
    FactoryLastSerie
)

from ..dto import UserType, WindowIndicatorType, WindowIndicatorConfig

class GenerateContentUseCase:

    def __init__(self, 
            factory_last_serie:FactoryLastSerie,
            factory_window_inidicator: Optional[FactoryWindowIndicator] = None ,
            serie_data: Optional[SeriesRepository] = None,
            users: Optional[SearchUsersInterface] = None,
            factory_send_email: Optional[FactorySendEmail] = None,
            factory_validate_user: Optional[FactoryValidateUser] = None,
            factory_generate_content_ia: Optional[FactoryGenerateContentIA] = None
            ):
        self.factory_last_serie = factory_last_serie
        self.window_indicator = factory_window_inidicator
        self.serie_data = serie_data
        self.users = users
        self.factory_send_email = factory_send_email
        self.factory_generate_content_ia = factory_generate_content_ia
        self.factory_validate_user = factory_validate_user

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

        serie = self.factory_last_serie.create_last_serie(user_type=UserType.PREMIUM.value)
        serie_info = serie.get_last_data(serie_id=serie_id)
        content = self.factory_generate_content_ia.create_generate_content_ia(UserType.PREMIUM.value)
        content_serie = content.generate_content(serie_info)

        return content_serie

    def generate_content_serie_with_inidicators(self, serie_id:int):
        """
        1. Obtener serie
        2. Obtener los usuarios
        3. Obtener el nombre y ultimo dato de la serie restringiedo el tipo de grafica por usuario 
        4. Validar usuario para cada tipo de indicador 
        5. Calcular indicador.
        6. Obtener ultimo dato de cada calculo del inidicador
        7. Por cada inidicador mandar el ultimo dato de la seria, nombre y el indicador correspondiente al prompt,
            el prompt tiene que variar por cada tipo de usuario
        8. Notificar via correo al usuario solo tipo pro, student y suscribed la generación del contenido

        1. series_repository
        2. search_user_interface
        3. factory_last_serie( necesita last_serie_data_interface)
        4. factory_validate_user (necesita validate_user_inteface)
        5. factory_window_inidicator (necesita window_indicator)
        6. None
        7. factory_generate_content_ia (necesita generate_content_ia)
        8. factory_send_email(necesita send_email_interface)
        """

        users = self.users.get_users()
        print(users)
        series_data = self.serie_data.get_series_data(serie_id)
        for user in users:
            serie = self.factory_last_serie.create_last_serie(user_type=user)
            serie_info = serie.get_last_data(serie_id=serie_id)
            if not serie_info:
                print ("No se puede generar esta gráfica para este usuario")
                continue
            for indicator in WindowIndicatorType:
                create_validation = self.factory_validate_user.create_calculate_indicator(user_type=user)
                indicator_type = create_validation.validate_user_with_indicator(indicator_type=indicator)
                if not indicator_type:
                    continue
                window_indicator = self.window_indicator.create_window_indicator(window_indicator_type=indicator_type)
                calculate_indicator = window_indicator.calculate(
                    series_data=series_data,
                    window_indicator_config=WindowIndicatorConfig(period=2)
                )
                last_indicator_data = calculate_indicator[-1]
                content = self.factory_generate_content_ia.create_generate_content_ia(type_user=user)
                generate_content = content.generate_content_with_indicator(
                    type_indicator=indicator,
                    serie_info=serie_info,
                    last_indicator_data= last_indicator_data
                )
                print(generate_content)
                email = self.factory_send_email.create_send_email(user_type=user)
                send_email = email.send_email_to_user(user_data=user)
                print(send_email)
            

            





            

