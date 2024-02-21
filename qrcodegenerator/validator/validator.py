from .base_validator import BaseValidator


class QrCodeValidator(BaseValidator):
    def __init__(self):
        super().__init__()
        self.required_fields = {
            "type": BaseValidator.is_type_field,
            "string_to_encode": BaseValidator.is_text_field,
        }
        self.optional_fields = {}
