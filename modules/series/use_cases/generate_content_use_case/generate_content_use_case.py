from .interfaces import GenerateContentIAInterface, LastSerieDataInterface, GetUserDataInterface, SendEmailInterface

class GenerateContentUseCase:

    def __init__(self,
        generate_content_ia:GenerateContentIAInterface,
        last_serie_data:LastSerieDataInterface,
        get_user_data:GetUserDataInterface,
        send_email:SendEmailInterface
    ):
        self.generate_content_ia = generate_content_ia
        self.last_serie_data = last_serie_data
        self.get_user_data = get_user_data
        self.send_email = send_email

    def generate_content_serie(self, serie_id:int, user_id:int):
        """
        1. Obtener el nombre y ultimo dato de la serie
        2. Obtener el prompt
        3. Enviar datos a la IA (Generar contenido)
        4. recibir respuesta
        5. Obtener datos de usuario
        6. Enviar correo a usuarios pro, student y subscribed

        1. last_serie_data_interface
        2. search_prompt_interface
        3. generate_content_ia_interface
        4. None
        5. get_user_data_interface
        6. send_email_interface
        """

        serie_info = self.last_serie_data.get_last_data(serie_id)
        content_serie = self.generate_content_ia.generate_content(serie_info)

        user = self.get_user_data.get_user(user_id)
        message = self.send_email.send_email(user)

        return content_serie, message

