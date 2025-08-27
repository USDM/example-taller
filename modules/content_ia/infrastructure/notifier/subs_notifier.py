from modules.content_ia.use_cases.content_video_use_case.interfaces import Notifier

class SubsNotifier(Notifier):

  def send_email(self, email:str):
    print(f"Sending email to {email}")
