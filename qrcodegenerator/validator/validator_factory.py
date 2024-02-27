from abc import ABC

from qrcodegenerator.validator.whatsapp_validator import QrCodeWhatsappValidator
from qrcodegenerator.validator.phone_validator import QrCodePhoneValidator
from qrcodegenerator.validator.validator import QrCodeValidator
from qrcodegenerator.validator.email_validator import QrCodeEmailValidator
from qrcodegenerator.validator.base_validator import BaseValidator
from qrcodegenerator.service.generators.types import (
    TYPE_PHONE,
    TYPE_TEXT,
    TYPE_URL,
    TYPE_WHATSAPP,
    TYPE_EMAIL,
)


class QrCodeValidatorFactory(ABC):
    @staticmethod
    def get_validator(type: str):
        if type == TYPE_PHONE:
            return QrCodePhoneValidator()
        elif type in [TYPE_TEXT, TYPE_URL]:
            return QrCodeValidator()
        elif type == TYPE_WHATSAPP:
            return QrCodeWhatsappValidator()
        elif type == TYPE_EMAIL:
            return QrCodeEmailValidator()
        elif type is None:
            return BaseValidator()
        return QrCodeValidator()
