from modules.content_ia.use_cases.generate_content_use_case.interfaces import Workflow, Notifier, FactoryUserContent as FactoryUserContentInterface
from ..notifier import NotifierFactory
from modules.content_ia.infrastructure.ia import FactoryIA
from modules.content_ia.use_cases.dto import PlanConfig
from dataclasses import dataclass
from ..workflow import FactoryWorkflow
from modules.content_ia.use_cases.shared import IA

@dataclass
class UserContentPlanConfig:
  workflow: Workflow
  notifier: Notifier
  ias: list[IA]

class FactoryUserContent(FactoryUserContentInterface):

  def create_using_plan_config(self, plan_config:PlanConfig) -> UserContentPlanConfig:
    workflow = FactoryWorkflow.create_using_plan_config(plan_config.analyze_apis)
    notifier = NotifierFactory.create_using_plan_config(plan_config.send_email)
    ias = [ FactoryIA.create(ia_name) for ia_name in plan_config.ia_names ]
    return UserContentPlanConfig(
      workflow=workflow,
      notifier=notifier,
      ias=ias
    )