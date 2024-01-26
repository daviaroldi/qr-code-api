from abc import ABC, abstractmethod

from .exception import ValidationDataError
from .phone_validator import QrCodePhoneValidator
from .validator import QrCodeValidator
from .base_validator import BaseValidator


class QrCodeValidatorFactory(ABC):
    @staticmethod
    def get_validator(type: str) -> BaseValidator:
        if type == "phone":
            return QrCodePhoneValidator()
        return QrCodeValidator()
