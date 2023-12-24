from abc import ABC, abstractmethod

from .generators.phone import PhoneQrCodeGenerator
from .generators.base import QrCodeGenerator


class QrCodeGeneratorFactory(ABC):
    @abstractmethod
    def get_qr_code_generator(type: str):
        if type == "phone":
            return PhoneQrCodeGenerator()
        return QrCodeGenerator()
