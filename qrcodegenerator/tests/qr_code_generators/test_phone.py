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
            "qr_code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAUoAAAFKAQAAAABTUiuoAAABW0lEQVR42u2awY2FMAxEo00BKYnWUxIFIHmD7SQg/cO/rDQrvRwQgbk9TTw2FPt29YIUKVKkSJFqSEuuOu7aNZ6ddTw95+PDpT/l64X0b6RJy3ksRtYHsnL4dr2Flg6t20eOp98GC1DnbTXfQkuUVhyQ01vQkqY16pbhrf9StxxPFC+jbonS2pnQDZYXMqEkrde6PjcA0JKh1df2DhiZMuwKW+EtuZOwpq2cW2T5tnowaMl5Ky4W6dBfbJdBS8pb+/w7V2Qv1aClSisc1eeZOHswMqGqt9aZ6HdtGoy6pdcdp7demTBDB7T0aIXB/LPJCh29keAFaU0f7byxF7REZxkPgx1zJEXdkuuOfVV7+m0NC/GWXt3KGfx76FSoW4K01vet3WVFycJbyrTWmZgzKGOWIU2rzojYjK+R4nUrzHQ+kUFLNRPmLLe8R/LQ0uy3+FUWKVKkSJEqS38BzhFdZ+jg5pAAAAAASUVORK5CYII="
        }
