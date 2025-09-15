from ...dto import UserData
from .generate_content_ia_interface import GenerateContentIAInterface
from typing import Protocol

class FactoryGenerateContentIA(Protocol):
    def create_generate_content_ia(self, type_user:UserData) -> GenerateContentIAInterface:
        pass
