from content_service.content_service import ContentService
from chat_content_service.chat_content_service import ChatContentService
from dto import SubcontentType
from content_service.content_repository import ContentRepository

"""
VAMOS A SUPONER QUE NOS LLEGAN NUEVOS REQUERIMIENTOS

1. Necesitamos que mas de 1 IA genere contenido
2. El chat debe ser con la IA que el usuario quiera

"""

def main():

    content_repository = ContentRepository()
    video_url = "https://www.youtube.com/watch?v=aa_GIiivHTw"
    
    #EN UN ENPOINT
    content_service = ContentService(content_repository)
    content_service.process_content_video(video_url)

    content_service.generate_video_subcontent(2, SubcontentType.SUMMARY)
    
    ## EN UN ENPOINT
    #chat_content_service = ChatContentService(content_repository)
    #chat_content_service.chat_with_content(1, SubcontentType.COMMENTS, "¿Cuál es el tema principal del video?")

    #content_service.generate_summary(1)
    #content_service.generate_questions(1)

    #content_service.generate_video_subcontent(1, SubcontentType.SUMMARY)
    

    
if __name__ == "__main__":
    main()