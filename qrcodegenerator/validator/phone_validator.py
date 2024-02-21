from .base_validator import BaseValidator


class QrCodePhoneValidator(BaseValidator):
    def __init__(self):
        super().__init__()
        self.required_fields = {
            "type": BaseValidator.is_type_field,
            "phone": BaseValidator.is_phone_number_valid,
            "country_code": BaseValidator.is_country_code_valid,
        }
        self.optional_fields = {}
