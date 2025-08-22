from abc import ABC, abstractmethod

class Notifier(ABC):

  @abstractmethod
  def send_email(self, email:str):
    pass

