import json

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from qrcodegenerator.service.qr_code_generator_factory import QrCodeGeneratorFactory


@require_POST
def index(request):
    body = json.loads(request.body)
    generator = QrCodeGeneratorFactory.get_qr_code_generator("type")
    return JsonResponse({"qr_code": generator.generate(body.get("string_to_encode"))})
