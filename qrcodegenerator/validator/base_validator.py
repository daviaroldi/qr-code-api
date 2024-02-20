from qrcodegenerator.validator.exception import ValidationDataError
from qrcodegenerator.service.generators.types import FREE_GENERATOR_TYPES


class BaseValidator:
    required_fields = {}
    optional_fields = {}

    REQUIRED_FIELD_MESSAGE = "Required field"

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
