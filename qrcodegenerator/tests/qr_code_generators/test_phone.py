import json
import pytest


class TestQRCodePhoneGenerator:
    @pytest.mark.parametrize(
        "body,response",
        [
            ({"type": "phone", "country_code": "55"}, {"phone": "Required field"}),
            ({"type": "phone", "phone": "5199911223344"}, {"country_code": "Required field"}),
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
