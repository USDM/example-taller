from ...use_cases.emails_use_case.interfaces.send_email_repository import SendEmailRepository
from ...use_cases.dto import Content
class SendEmail(SendEmailRepository):
    def send_email(self, email:str, contents:list[Content]):
        print(f""" 
        Se envia correo a { email }
        Con sus contenidos
        { contents }
        """)