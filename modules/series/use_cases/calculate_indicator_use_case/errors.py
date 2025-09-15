class InsufficientDataError(Exception):
        
    def __init__(self, series_id: int):
        self.series_id = series_id
        super().__init__(f"La serie {series_id} no tiene suficientes datos para calcular el indicador")

class UserTypeIndicatorNotAllowedError(Exception):
        
    def __init__(self, user_type:str, window_indicator_type:str):
        super().__init__(f"El tipo de usuario {user_type} no tiene acceso a calcular el indicador {window_indicator_type}")
