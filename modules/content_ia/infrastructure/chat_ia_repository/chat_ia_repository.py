from  ...use_cases.shared.base_ia import IA, IAMessage
from ...use_cases.dto import Content

class ChatIARepository:

    def __init__(self, ia: IA):
        self.ia = ia

    def chat(self, content: Content, message: str) -> str:
        prompt = f"""
        You are a helpful assistant that can answer questions about the following content:
        {content}

        the user is asking: {message}
        return the answer in spanish
        """
        return self._send_prompt(prompt, is_json=False)
        
    def _send_prompt(self, prompt:str, is_json:bool) -> str:
        messages = [
        IAMessage(role="user", content=prompt)
        ]
        response = self.ia.send_prompt(messages, is_json)
        return response.content