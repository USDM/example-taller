from ...use_cases.emails_use_case.emails_use_case import EmailsUseCase
from modules.content_ia.infrastructure.search_content_by_user_repository import search_content_by_user_id



from modules.content_ia.infrastructure.search_content_by_user_repository import SearchContentByUserId
from modules.content_ia.infrastructure.send_email_repository import SendEmail

def create_send_email_use_case():
    send_mail = SendEmail()
    search_content_by_user_id = SearchContentByUserId()
    return EmailsUseCase(search_content_by_user_id, send_mail)
        
