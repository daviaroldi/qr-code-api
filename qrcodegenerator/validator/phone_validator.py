from .base_validator import BaseValidator

from phonenumbers.phonenumberutil import region_code_for_country_code


class QrCodePhoneValidator(BaseValidator):
    def __init__(self):
        self.required_fields = {
            "type": BaseValidator.is_type_field,
            "phone": "phone_number",
            "country_code": QrCodePhoneValidator.is_country_code_valid,
        }
        self.optional_fields = {}

    @staticmethod
    def is_country_code_valid(value):
        try:
            return int(value) and region_code_for_country_code(int(value)) != "ZZ"
        except ValueError:
            return False
