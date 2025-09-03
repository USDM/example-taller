from .interfaces import SearchContentRepository
from .interfaces import ChatIARepository
class ChatWithContentUseCase:

    """
        Recibir un ide de contednido OK
        Recibir una pregunta de usuario OK
        Mandar contenido y pregunta al modelo de IA
        Mostrar respuesta de la IA
    """

    def __init__(self, 
    search_content_repository: SearchContentRepository,
    chat_ia_repository: ChatIARepository):
        self.search_content_repository = search_content_repository
        self.chat_ia_repository = chat_ia_repository

    def chat_with_content(self, content_id: int, question: str):
        #buscar el contenido -> repositorio para buscar el contenido        
        content = self.search_content_repository.search_content(content_id)
        comments = content["comments"]
        respuesta = self.chat_ia_repository.send_prompt(question, comments)
        print(respuesta)