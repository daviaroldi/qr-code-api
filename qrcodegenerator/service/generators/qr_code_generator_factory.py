from abc import ABC, abstractmethod

from qrcodegenerator.service.generators.phone import QrCodePhoneGenerator
from qrcodegenerator.service.generators.base import QrCodeGenerator


class QrCodeGeneratorFactory(ABC):
    TYPE_PHONE = "phone"

    TYPES = [TYPE_PHONE]

    @staticmethod
    def get_generator(type: str):
        if type == "phone":
            return QrCodePhoneGenerator()
        return QrCodeGenerator()
