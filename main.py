"""

Nos solicitan que rodolfo ficticio pueda buscar series por nombre 
cuando escribe un nombre de serie incompleto le tiene que enviar todas las series que coincidan con el nombre que escribio


"""

from modules.content_ia.infrastructure.factory_use_cases import create_generate_content_use_case

from modules.series.infrastructure.factory_use_cases import create_series_service, create_calculate_indicator_use_case
from modules.series.use_cases.dto import SourceName, WindowIndicatorType, WindowIndicatorConfig 
from modules.content_ia.use_cases.dto import SourceType

from modules.content_ia.infrastructure.factory_use_cases import create_chat_ia_use_case

def main():

    chat_ia_use_case = create_chat_ia_use_case(message="Que comentario es el que mas se acerca a la realidad?", content_id=1)
    print(chat_ia_use_case)
    return

    # video_url = "https://www.youtube.com/watch?v=aa_GIiivHTw"
    # source_path = "media/test.pdf"
    # tweet_path = "media/fake_1.PNG"
    # user_id = 4
    # content_service = create_generate_content_use_case()
    # content_service.process_content(tweet_path, user_id, SourceType.TWEET)

    # return

    #series_service = create_series_service()
    #series_service.search_match_series("APP", SourceName.TRADING, 3)

    window_indicator_type = WindowIndicatorType.RSI
    window_indicator_config = WindowIndicatorConfig(period=100000000)

    calculate_indicator_use_case = create_calculate_indicator_use_case()
    calculate_indicator_use_case.calculate_window_indicator(1, window_indicator_type, window_indicator_config)


if __name__ == "__main__":
    main()