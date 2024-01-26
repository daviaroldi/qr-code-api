from .base_validator import BaseValidator


class QrCodePhoneValidator(BaseValidator):
    required_fields = {
        "type": BaseValidator.is_type_field,
        "phone": "phone_number",
        "country_code": "country_code",
    }
    optional_fields = {}
