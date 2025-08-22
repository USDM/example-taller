from .notifier import Notifier

class NullEmail(Notifier):

  def send_email(self, email:str):
    pass