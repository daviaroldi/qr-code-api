import json

from django.views.decorators.http import require_POST
from qrcodegenerator.service import QrCodeService
from qrcodegenerator.decorator import bad_request


@require_POST
@bad_request
def index(request):
    body = json.loads(request.body)
    service = QrCodeService()

    return service.generate(body)
