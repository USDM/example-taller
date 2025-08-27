class InsufficientDataError(Exception):
        
    def __init__(self, series_id: int):
        self.series_id = series_id
        super().__init__(f"La serie {series_id} no tiene suficientes datos para calcular el indicador")