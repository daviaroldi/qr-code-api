from .base_validator import BaseValidator


class QrCodeValidator(BaseValidator):
    required_fields = {"type": BaseValidator.is_type_field}
    optional_fields = {}
