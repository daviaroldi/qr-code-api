from abc import ABC

from qrcodegenerator.service.generators.types import (
    TYPE_URL,
    TYPE_PHONE,
    TYPE_TEXT,
    TYPE_WHATSAPP,
    TYPE_EMAIL,
)
from qrcodegenerator.service.generators.phone import QrCodePhoneGenerator
from qrcodegenerator.service.generators.base import QrCodeGenerator
from qrcodegenerator.service.generators.whatsapp import QrCodeWhatsappGenerator
from qrcodegenerator.service.generators.email import QrCodeEmailGenerator


class QrCodeGeneratorFactory(ABC):
    @staticmethod
    def get_generator(type: str):
        if type == TYPE_PHONE:
            return QrCodePhoneGenerator()
        elif type in [TYPE_TEXT, TYPE_URL]:
            return QrCodeGenerator()
        elif type == TYPE_WHATSAPP:
            return QrCodeWhatsappGenerator()
        elif type == TYPE_EMAIL:
            return QrCodeEmailGenerator()

        return QrCodeGenerator()
