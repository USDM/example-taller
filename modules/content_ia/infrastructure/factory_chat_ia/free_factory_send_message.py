from modules.content_ia.use_cases.chat_ia_use_case.interfaces.i_send_message import ISendMessage
from modules.content_ia.use_cases.dto import PlanConfig

class FreeFactorySendMessage(ISendMessage):
    def send_message(self, message: str, plan_config: PlanConfig, max_messages: int) -> str:
        if max_messages > plan_config.max_messages:
            raise Exception("Haz llegado al límite de mensajes en tu plan")
        
        print("Desde la implementacion de free")
    