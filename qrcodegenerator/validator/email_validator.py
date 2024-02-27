from .base_validator import BaseValidator


class QrCodeEmailValidator(BaseValidator):
    def __init__(self):
        super().__init__()
        self.required_fields = {
            "type": BaseValidator.is_type_field,
            "email": BaseValidator.is_email_valid,
            "subject": BaseValidator.is_text_field,
            "message": BaseValidator.is_text_field,
        }
        self.optional_fields = {}
