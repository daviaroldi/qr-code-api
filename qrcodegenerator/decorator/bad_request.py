import functools

from django.http import JsonResponse


def bad_request(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # TODO made on this way to avoid circular import of ValidationDataError
            # check how to fix it
            if hasattr(e, "message") and hasattr(e, "code"):
                json_response = JsonResponse(e.message)
                json_response.status_code = e.code
                return json_response
            else:
                raise e

    return wrapper
