from typing import Protocol

from ...dto import WindowIndicatorType, WindowIndicatorData

class LastIndicatorDataInterface(Protocol):
    def get_last_indicator_data(self, indicator_data: list[WindowIndicatorData]) -> WindowIndicatorData :
        pass