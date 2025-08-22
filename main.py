from content_service.content_service import ContentService
from chat_content_service.chat_content_service import ChatContentService
from dto import SubcontentType, IANames
from content_service.content_repository.content_repository import ContentRepository
from content_service.content_video_generator import ProContentVideoGenerator
from dto import UserType
from content_service.factory_user_content import FreeFactoryUserContent, SuscribeFactoryUserContent, ProFactoryUserContent

"""
VAMOS A SUPONER QUE NOS LLEGAN NUEVOS REQUERIMIENTOS

1. Se necesita que
Para usuario free, se genere solo el contenido pero que no guarde en base de datos, gemini
Para usuarios suscritos, se haga el proceso normal pero enviando un correo al usuario al final del proceso, gemini, claude
Para usuarios premium, se haga el proceso normal, con envio de correo al usuario al final del proceso y conexion a apis, gemini, claude, chatgpt, grok
que nos sirven para mejorar la experiencia del usuario en nuestra plataforma

"""

def main():

    #content_repository = ContentRepository()
    video_url = "https://www.youtube.com/watch?v=aa_GIiivHTw"
    
    user_type = UserType.STUDENT

    #EN UN ENPOINT
    content_service = ContentService()
    content_service.process_content_video(video_url, user_type, 0)


    #content_service.generate_video_subcontent(2, SubcontentType.SUMMARY)

    #chat_content_service = ChatContentService(content_repository)
    #ia_name = "gemini"

    #ia_name_enum = IANames(ia_name)

    #chat_content_service.chat_with_content(1, SubcontentType.COMMENTS, "¿Cuál es el tema principal del video?", ia_name_enum)
    
    ## EN UN ENPOINT
    #chat_content_service = ChatContentService(content_repository)
    #chat_content_service.chat_with_content(1, SubcontentType.COMMENTS, "¿Cuál es el tema principal del video?")

    #content_service.generate_summary(1)
    #content_service.generate_questions(1)

    #content_service.generate_video_subcontent(1, SubcontentType.SUMMARY)
    

    
if __name__ == "__main__":
    main()