import json
import pytest


class TestQRCodePhoneGenerator:
    @pytest.mark.parametrize(
        "body,response",
        [
            ({"type": "phone", "country_code": "55"}, {"phone": "Required field"}),
            (
                {"type": "phone", "phone": "5199911223344"},
                {"country_code": "Required field"},
            ),
            (
                {"phone": "5199911223344", "country_code": "55"},
                {"type": "Required field"},
            ),
        ],
    )
    def test_missing_fields(self, client, body, response):
        request_response = client.post(
            "/qr-code-generator/", body, content_type="application/json"
        )

        # Check that the response is 400 BadRequest.
        assert request_response.status_code == 400

        # Check error message for phone field
        content_decoded = json.loads(request_response.content)
        assert content_decoded == response

    @pytest.mark.parametrize(
        "body,response",
        [
            (
                {"type": "phone", "country_code": "asdfe", "phone": "5199911223344"},
                {"country_code": "Invalid value"},
            ),
            (
                {"type": "phone", "country_code": False, "phone": "5199911223344"},
                {"country_code": "Invalid value"},
            ),
            (
                {"type": "phone", "country_code": None, "phone": "5199911223344"},
                {"country_code": "Invalid value"},
            ),
        ],
    )
    def test_wrong_fields(self, client, body, response):
        request_response = client.post(
            "/qr-code-generator/", body, content_type="application/json"
        )

        # Check that the response is 400 BadRequest.
        assert request_response.status_code == 400

        # Check error message for phone field
        content_decoded = json.loads(request_response.content)
        assert content_decoded == response

    def test_correct_result(self, client):
        body = {"type": "phone", "country_code": "55", "phone": "5199911223344"}
        request_response = client.post(
            "/qr-code-generator/", body, content_type="application/json"
        )

        # Check that the response is 400 BadRequest.
        assert request_response.status_code == 200

        # Check error message for phone field
        content_decoded = json.loads(request_response.content)
        assert content_decoded == {
            "qr_code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAKUAAAClAQAAAAAVUAB3AAABEklEQVR42u1WMQ6DMAw8ypAxT8hP4GNIIPEx+pM8gTEDwj27DB26VbZaqRkCeDnd+c4G8uY0/KvfX90BdHtf5S4HXzFLu+Hd+byqaLMYUBswFft0RZuQ7rIUXkchywg0qqrcYtD2XoK4ad92FNnyEdA38+TEvpGluyevU19y4Ym28JHXSpfMNfkrWeTMixpz1eS5c2vIB9KWxQj6cuurRS0Rt0SgkdZCOcHkbQHcRpVzZN9a59w3mpDcLk+2gB2AgUoyBkrQfXIpI7MKgmaJNk8HMglKwJx8boPi70nbAYzBSSCMIfvNooaAvBmaysmfEyMYgFbSmVfx36bWNy4bvfzzZiJyIGu6ZYvZ3f9/+1+qPgCwOoLH8JWOMAAAAABJRU5ErkJggg=="
        }
