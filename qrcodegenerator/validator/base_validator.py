from qrcodegenerator.validator.exception import ValidationDataError
from qrcodegenerator.service.generators.types import FREE_GENERATOR_TYPES
from phonenumbers.phonenumberutil import region_code_for_country_code


class BaseValidator:
    REQUIRED_FIELD_MESSAGE = "Required field"

    def __init__(self):
        self.required_fields = {"type": BaseValidator.is_type_field}
        self.optional_fields = {}

    def validate(self, values):
        # validate if all required fields are informed
        errors = {
            field: self.REQUIRED_FIELD_MESSAGE
            for field in self.required_fields
            if field not in values
        }

        # validate values against the required type TODO
        if not errors:
            for field in self.required_fields:
                func = self.required_fields[field]
                if callable(func) and not func(values[field]):
                    errors[field] = "Invalid value"

        if errors:
            raise ValidationDataError(errors)

    @staticmethod
    def is_type_field(value):
        return value and isinstance(value, str) and value in FREE_GENERATOR_TYPES

    @staticmethod
    def is_text_field(value):
        return value and isinstance(value, str)

    @staticmethod
    def is_country_code_valid(value):
        try:
            return (
                value
                and int(value)
                and region_code_for_country_code(int(value)) != "ZZ"
            )
        except ValueError:
            return False

    @staticmethod
    def is_phone_number_valid(value):
        try:
            return value and int(value) and True  # TODO refactor this validation
        except ValueError:
            return False
