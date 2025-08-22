from .notifier import Notifier

class SubsNotifier(Notifier):

  def send_email(self, email:str):
    print(f"Sending email to {email}")
