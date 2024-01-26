from django.core.exceptions import BadRequest
from django.http import JsonResponse

from qrcodegenerator.service.generators.qr_code_generator_factory import (
    QrCodeGeneratorFactory,
)
from qrcodegenerator.validator import QrCodeValidatorFactory


class QrCodeService:
    def generate(self, body) -> JsonResponse:
        type = body.get("type")

        QrCodeValidatorFactory.get_validator(type).validate(body)

        generator = QrCodeGeneratorFactory.get_generator(type)

        return JsonResponse({"qr_code": generator.generate(body)})
