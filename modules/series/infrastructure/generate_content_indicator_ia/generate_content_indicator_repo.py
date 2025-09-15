from ...use_cases.generate_content_indicator_use_case.interfaces import IGenerateContentIndicatorIA
from ..ia.gemini import GeminiIA
from ...use_cases.shared.base_ia import IAMessage
from ...use_cases.dto import ContentSerie

class GenerateContentIndicatorIA(IGenerateContentIndicatorIA):
    def generate_content_indicator_ia(self, prompt:str) -> ContentSerie:
        response = self._send_prompt(prompt, is_json=True)
        content_serie = ContentSerie(
            comments=response["comments"] if "comments" in response else [],
            summary=response["summary"] if "summary" in response else "",
            projections=response["projections"] if "projections" in response else "",
            confidence = response["confidence"] if "confidence" in response else 0,
            risk = response["risk"] if "risk" in response else 0,
            trend = response["trend"] if "trend" in response else "",
            recommendation = response["recommendation"] if "recommendation" in response else "",
        )
        return content_serie


    def _send_prompt(self, prompt:str, is_json:bool) -> str:
        messages = [
            IAMessage(role="user", content=prompt)
        ]
        response = GeminiIA().send_prompt(messages, is_json)
        return response.content