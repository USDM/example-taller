from .workflow import Workflow

class NullWorkflow(Workflow):

  def after_process(self, user_id:int):
    pass
