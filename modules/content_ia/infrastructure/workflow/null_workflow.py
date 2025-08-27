from modules.content_ia.use_cases.generate_content_use_case.interfaces import Workflow

class NullWorkflow(Workflow):

  def after_process(self, user_id:int):
    pass
