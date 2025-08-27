"""

Nos solicitan que rodolfo ficticio pueda buscar series por nombre 
cuando escribe un nombre de serie incompleto le tiene que enviar todas las series que coincidan con el nombre que escribio


"""

from modules.content_ia.infrastructure.factory_use_cases.factory_video_use_case import create_content_service

from modules.series.infrastructure.factory_use_cases import create_series_service, create_calculate_indicator_use_case
from modules.series.use_cases.dto import SourceName, WindowIndicatorType, WindowIndicatorConfig

def main():

    """

    video_url = "https://www.youtube.com/watch?v=aa_GIiivHTw"
    user_id = 1
    content_service = create_content_service()
    content_service.process_content_video(video_url, user_id)

    """

    #series_service = create_series_service()
    #series_service.search_match_series("APP", SourceName.TRADING, 3)

    window_indicator_type = WindowIndicatorType.RSI
    window_indicator_config = WindowIndicatorConfig(period=3)

    calculate_indicator_use_case = create_calculate_indicator_use_case()
    calculate_indicator_use_case.calculate_window_indicator(1, window_indicator_type, window_indicator_config)


if __name__ == "__main__":
    main()