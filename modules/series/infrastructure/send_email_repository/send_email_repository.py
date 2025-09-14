from ...use_cases.generate_content_use_case.interfaces import SendEmailInterface
from ...use_cases.dto import UserData

class SendEmailRepository(SendEmailInterface):

    def send_email_to_users(self, users:list[UserData]): 
        for user in users:
            if user.user_type in ["subscribed", "premium", "student"]:
                print(f"""
                    Correo enviado para usuario {user.user_email}
                    con tipo {user.user_type}
                """)

