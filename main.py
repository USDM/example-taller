from content_service.content_service import ContentService
from chat_content_service.chat_content_service import ChatContentService
from dto import SubcontentType, IANames
from content_service.content_repository.content_repository import ContentRepository
from content_service.content_video_generator import ProContentVideoGenerator
from dto import UserType
from content_service.factory_user_content import FreeFactoryUserContent, SuscribeFactoryUserContent, ProFactoryUserContent
from content_service.user_repository import MemoryUserRepository
from content_service.user_repository.factory_user_repository import FactoryUserRepository

"""
VAMOS A SUPONER QUE NOS LLEGAN NUEVOS REQUERIMIENTOS

1. Se necesita una configuracion por parte del administrador para decidir
ias
envio de correo
analisis de apis

"""

def main():

    FactoryUserRepository()

    #content_repository = ContentRepository()
    video_url = "https://www.youtube.com/watch?v=aa_GIiivHTw"

    user_id = 2

    #EN UN ENPOINT
    content_service = ContentService()
    content_service.process_content_video(video_url, user_id)


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

