from typing import Optional

from .interfaces import (
    LastSerieDataInterface,
    FactoryWindowIndicator,
    SeriesRepository,
    SearchUsersInterface,
    SendEmailInterface,
    ValidateUserInterface,
    FactoryGenerateContentIA
)

from ..dto import UserType, WindowIndicatorType, WindowIndicatorConfig

class GenerateContentUseCase:

    def __init__(self, 
            last_serie_data:LastSerieDataInterface,
            factory_window_inidicator: Optional[FactoryWindowIndicator] = None ,
            serie_data: Optional[SeriesRepository] = None,
            users: Optional[SearchUsersInterface] = None,
            send_email: Optional[SendEmailInterface] = None,
            validate_user: Optional[ValidateUserInterface] = None,
            factory_generate_content_ia: Optional[FactoryGenerateContentIA] = None
            ):
        self.last_serie_data = last_serie_data
        self.window_indicator = factory_window_inidicator
        self.serie_data = serie_data
        self.users = users
        self.send_email = send_email
        self.validate_user = validate_user
        self.factory_generate_content_ia = factory_generate_content_ia

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
        content = self.factory_generate_content_ia.create_generate_content_ia(UserType.PREMIUM.value)
        content_serie = content.generate_content(serie_info)

        return content_serie

    def generate_content_serie_with_inidicators(self, serie_id:int):
        """
        1. Obtener serie
        2. Obtener los usuarios
        3. Obtener el nombre y ultimo dato de la serie
        4. Validar usuario para cada tipo de indicador 
        5. Calcular indicador.
        6. Obtener ultimo dato de cada calculo del inidicador
        7. Por cada inidicador mandar el ultimo dato de la seria, nombre y el indicador correspondiente al prompt,
            el prompt tiene que variar por cada tipo de usuario
        8. Notificar via correo al usuario solo tipo pro, student y suscribed la generación del contenido

        1. series_repository
        2. search_user_interface
        3. last_serie_data_interface
        4. validate_user_interface
        5. factory_window_inidicator (necesita window_indicator)
        6. None
        7. factory_generate_content_ia (necesita generate_content_ia)
        8. send_email_interface
        """

        users = self.users.get_users()
        print(users)
        series_data = self.serie_data.get_series_data(serie_id)
        serie_info = self.last_serie_data.get_last_data(serie_id)
        for indicator in WindowIndicatorType:
            for user in users:
                validate_user = self.validate_user.validate_user_with_indicator(
                    user_data=user,
                    indicator=indicator
                )
                if validate_user:
                    print(f"""
                        Calculo de inidcador {indicator.value} a realizar para
                        usuario {user.user_email} con tipo {user.user_type}
                    """)
                    window_indicator = self.window_indicator.create_window_indicator(
                                                                window_indicator_type=indicator
                                                                )
                    calculate_indicator = window_indicator.calculate(
                        series_data=series_data,
                        window_indicator_config=WindowIndicatorConfig(period=2)
                    )
                    last_indicator_data = calculate_indicator[-1]
                    content = self.factory_generate_content_ia.create_generate_content_ia(
                        type_user=user
                    )
                    generate_content = content.generate_content_with_indicator(
                        type_indicator=indicator,
                        serie_info=serie_info,
                        last_indicator_data= last_indicator_data
                    )
                    print(generate_content)
                else:
                    print(f"""
                        Calculo de inidcador {indicator.value} NO realizado para
                        usuario {user.user_email} con tipo {user.user_type}
                    """)

        self.send_email.send_email_to_users(users)
            

            





            

