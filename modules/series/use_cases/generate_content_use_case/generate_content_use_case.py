from .interfaces import GenerateContentIAInterface, LastSerieDataInterface

class GenerateContentUseCase:

    def __init__(self, generate_content_ia:GenerateContentIAInterface, last_serie_data:LastSerieDataInterface):
        self.generate_content_ia = generate_content_ia
        self.last_serie_data = last_serie_data

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

