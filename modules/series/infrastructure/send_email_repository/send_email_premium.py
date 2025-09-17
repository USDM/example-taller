from ...use_cases.generate_content_use_case.interfaces import SendEmailInterface
from ...use_cases.dto import UserData

class SendEmailPremium(SendEmailInterface):

    def send_email_to_user(self, user_data:UserData) -> str:
        return f"""
                    Correo enviado para usuario {user_data.user_email}
                    con tipo {user_data.user_type}
                """