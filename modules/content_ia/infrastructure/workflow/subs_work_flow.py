from modules.content_ia.use_cases.generate_content_use_case.interfaces import Workflow

class SubsWorkFlow(Workflow):

  def after_process(self, user_id:int):
    print(f"CONEXION A APIS PARA MEJORAR EXPERIENCIA DE USUARIO {user_id}")