from abc import ABC

from .phone_validator import QrCodePhoneValidator
from .validator import QrCodeValidator
from ..service.generators.types import TYPE_PHONE, TYPE_TEXT, TYPE_URL


class QrCodeValidatorFactory(ABC):
    @staticmethod
    def get_validator(type: str):
        if type == TYPE_PHONE:
            return QrCodePhoneValidator()
        elif type in [TYPE_TEXT, TYPE_URL]:
            return QrCodeValidator()
        return QrCodeValidator()
