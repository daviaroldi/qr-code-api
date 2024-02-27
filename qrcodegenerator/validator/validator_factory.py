from abc import ABC

from .whatsapp_validator import QrCodeWhatsappValidator
from .phone_validator import QrCodePhoneValidator
from .validator import QrCodeValidator
from .base_validator import BaseValidator
from ..service.generators.types import TYPE_PHONE, TYPE_TEXT, TYPE_URL, TYPE_WHATSAPP


class QrCodeValidatorFactory(ABC):
    @staticmethod
    def get_validator(type: str):
        if type == TYPE_PHONE:
            return QrCodePhoneValidator()
        elif type in [TYPE_TEXT, TYPE_URL]:
            return QrCodeValidator()
        elif type == TYPE_WHATSAPP:
            return QrCodeWhatsappValidator()
        elif type is None:
            return BaseValidator()
        return QrCodeValidator()
