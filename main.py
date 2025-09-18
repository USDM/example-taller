"""

Nos solicitan que rodolfo ficticio pueda buscar series por nombre 
cuando escribe un nombre de serie incompleto le tiene que enviar todas las series que coincidan con el nombre que escribio


"""

from modules.content_ia.infrastructure.factory_use_cases import create_generate_content_use_case

from modules.series.infrastructure.factory_use_cases import create_series_service, create_calculate_indicator_use_case
from modules.series.use_cases.dto import SourceName, WindowIndicatorType, WindowIndicatorConfig 
from modules.content_ia.use_cases.dto import SourceType

from modules.content_ia.use_cases.chat_ia_use_case.chat_ia_use_case import ChatIAUseCase
from modules.content_ia.search_content_repository.memory_search_content_repository import MemorySearchContentRepository

from modules.content_ia.infrastructure.factory_use_cases import create_chat_ia_use_case

from modules.content_ia.use_cases.emails_use_case import EmailsUseCase

from modules.content_ia.infrastructure.factory_use_cases import create_send_email_use_case
from modules.series.infrastructure.factory_use_cases import create_generate_content_with_indicator_use_case, create_generate_content_use_case

from modules.common.tables import TableResponseIa

from modules.series.use_cases.generate_content_use_case import GenerateContentUseCase
from modules.content_ia.infrastructure.factory_use_cases import create_chat_ia_comments_use_case


def main():

    """
        Ejercicio principal: Generar contenido de series con indicadores
            Objetivo: Apartir de una serie generar contenido con ia (Comentarios, resumen y proyecciones).
            Reglas de negocio:
            -Utilizar el ultimo dato de la serie
            -Utilizar el ultimo dato de cada uno de los indicadores
            -Por cada indicador generar el contenido de la serie
    """

    # content_generator = create_generate_content_with_indicator_use_case()
    # content_generator.generate_content_serie_with_inidicators(1)

    """
        Ejercicio 1: Enviar una notificacion por correo, solo para usuarios, pro, student, suscribed
            Objetivo: Apartir de una serie generar contenido con ia (Comentarios, resumen y proyecciones)
            y de acuerdo al tipo de usuario generar una notifiación por correo.
            Reglas de negocio:
            -Utilizar el ultimo dato de la serie
            -Restringir el calculo de indicadores por tipo de usuario, pro (todos los indicadores), student ( todos los indicadores), 
             free (solo sma), suscribed ( sma, roc, rsi)
            -Utilizar el ultimo dato de cada uno de los indicadores
            -Por cada indicador generar el contenido de la serie
            -El prompt se limitara para usuarios free (solo comentarios y menos caracteres), para los demas tipos generar todo el contenido pero 
            aumentando caracteres por cada uno
            -Los usuarios tipo pro, student y suscribed se les notifica via correo la generación de este contenido
            -Los usuarios free no puede obtener datos de unrate
    """


    """
        Ejercicio 2: Consultar historial de chats y hacer resumen
        Objetivo: De acuerdo a un arreglo de comentarios almacenados por un usuario, mostrar un resumen.
        Reglas de negocio:
            -Por cada tipo de usuario se tiene que hacer lo siguiente:
                fre: solo puede consultar 5 mensajes como maximo y tendra un prompt no muy especializiado para hacer el resumen
                suscribed: solo puede consultar 100 mensajes como maximo y tendra un prompt un poco mas especializado con respuesta en html para hacer el resumen
                student y premium: puede consultar todos los mensaje que haya y tendra un prompt especializado cn respuesta en html con una opinion constructiva
    """

    resume_generator = create_chat_ia_comments_use_case()
    resume_generator.generate_resume_comments(user_id=2)

    # content_generator = create_generate_content_with_indicator_use_case()
    # content_generator.generate_content_serie_with_inidicators(1)

    # content_generator = create_generate_content_use_case()
    # content =content_generator.generate_content_serie(1)
    # print(content)

    # chat_ia_use_case = create_chat_ia_use_case()
    # for pasda in [1,2,3]:
    #     chat_ia_use_case.chatWithContentIa(1, "que comentarios te mande?")
    # print(TableResponseIa().data)

    # email_use_case = create_send_email_use_case()
    # email_use_case.send_email(1)

    # video_url = "https://www.youtube.com/watch?v=aa_GIiivHTw"
    # source_path = "media/test.pdf"
    # tweet_path = "media/fake_1.PNG"
    # user_id = 4
    # content_service = create_generate_content_use_case()
    # content_service.process_content(tweet_path, user_id, SourceType.TWEET)

    # series_service = create_series_service()
    # series_service.search_match_series("APP", SourceName.GOOGLE, 3)

    # window_indicator_type = WindowIndicatorType.MACD
    # window_indicator_config = WindowIndicatorConfig(period=2)

    # calculate_indicator_use_case = create_calculate_indicator_use_case()
    # calculate_indicator_use_case.calculate_window_indicator(1, window_indicator_type, window_indicator_config)


if __name__ == "__main__":
    main()