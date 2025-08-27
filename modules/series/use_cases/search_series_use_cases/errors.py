
class TokenEmptyError(Exception):
        
    def __init__(self, source_name: str):
        self.source_name = source_name
        super().__init__(f"El token de la API de {source_name} está vacío en el archivo .env")



class APINotResponseError(Exception):
        
    def __init__(self, source_name: str):
        self.source_name = source_name
        super().__init__(f"La API de {source_name} no respondió")


class UserTypeNotAllowedError(Exception):
        
    def __init__(self, user_email:str, user_type:str, source_name:str):
        super().__init__(f"El usuario {user_email} con tipo {user_type} no tiene acceso a la fuente {source_name}")
