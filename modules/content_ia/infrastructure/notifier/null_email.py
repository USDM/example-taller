from modules.content_ia.use_cases.generate_content_use_case.interfaces import Notifier

class NullEmail(Notifier):

  def send_email(self, email:str):
    pass