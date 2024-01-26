import functools

from django.http import JsonResponse

from qrcodegenerator.validator.exception import ValidationDataError


def bad_request(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationDataError as e:
            json_response = JsonResponse(e.message)
            json_response.status_code = e.code
            return json_response

    return wrapper
