import json
import pytest


class TestQRCodeBaseGenerator:
    @pytest.mark.parametrize(
        "body,response",
        [
            ({"type": "text"}, {"string_to_encode": "Required field"}),
            (
                {"string_to_encode": "http://google.com"},
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
