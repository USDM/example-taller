from typing import Protocol

class ResumeCommentsRepository(Protocol):
    def resume_ia_prompt(self, comments:list) -> str:
        pass