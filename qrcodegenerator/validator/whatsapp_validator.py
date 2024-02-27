from .phone_validator import QrCodePhoneValidator
from .base_validator import BaseValidator


class QrCodeWhatsappValidator(QrCodePhoneValidator):
    def __init__(self):
        super().__init__()
        self.required_fields.update({"message": BaseValidator.is_text_field})
        self.optional_fields = {}
