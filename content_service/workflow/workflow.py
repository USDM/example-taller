from abc import ABC, abstractmethod

class Workflow(ABC):

  @abstractmethod
  def after_process(self, user_id:int):
    pass
