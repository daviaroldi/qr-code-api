import json
import pytest


class TestQRCodeEmailGenerator:
    @pytest.mark.parametrize(
        "body,response",
        [
            (
                {
                    "type": "email",
                    "email": "test@test.com",
                    "subject": "Testing subject",
                },
                {"message": "Required field"},
            ),
            (
                {
                    "type": "email",
                    "email": "test@test.com",
                    "message": "Testing message",
                },
                {"subject": "Required field"},
            ),
            (
                {
                    "type": "email",
                    "subject": "Testing subject",
                    "message": "Testing message",
                },
                {"email": "Required field"},
            ),
            (
                {
                    "email": "test@test.com",
                    "subject": "Testing subject",
                    "message": "Testing message",
                },
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
        "email",
        ["test", "test@testcom", "test.com", None, False, True, {}, []],
    )
    def test_invalid_email(self, client, email):
        body = {
            "type": "email",
            "email": email,
            "subject": "Testing subject",
            "message": "Testing message",
        }
        request_response = client.post(
            "/qr-code-generator/", body, content_type="application/json"
        )

        # Check that the response is 400 BadRequest.
        assert request_response.status_code == 400

        # Check error message for phone field
        content_decoded = json.loads(request_response.content)
        assert content_decoded == {"email": "Invalid value"}

    @pytest.mark.parametrize(
        "subject",
        [None, False, True, {}, []],
    )
    def test_subject_email(self, client, subject):
        body = {
            "type": "email",
            "email": "test@test.com",
            "subject": subject,
            "message": "Testing message",
        }
        request_response = client.post(
            "/qr-code-generator/", body, content_type="application/json"
        )

        # Check that the response is 400 BadRequest.
        assert request_response.status_code == 400

        # Check error message for phone field
        content_decoded = json.loads(request_response.content)
        assert content_decoded == {"subject": "Invalid value"}

    @pytest.mark.parametrize(
        "message",
        [None, False, True, {}, []],
    )
    def test_subject_email(self, client, message):
        body = {
            "type": "email",
            "email": "test@test.com",
            "subject": "Testing subject",
            "message": message,
        }
        request_response = client.post(
            "/qr-code-generator/", body, content_type="application/json"
        )

        # Check that the response is 400 BadRequest.
        assert request_response.status_code == 400

        # Check error message for phone field
        content_decoded = json.loads(request_response.content)
        assert content_decoded == {"message": "Invalid value"}

    def test_correct_result(self, client):
        body = {
            "type": "email",
            "email": "test@test.com",
            "subject": "Testing subject",
            "message": "Testing message",
        }
        request_response = client.post(
            "/qr-code-generator/", body, content_type="application/json"
        )

        # Check that the response is 400 BadRequest.
        assert request_response.status_code == 200

        # Check error message for phone field
        content_decoded = json.loads(request_response.content)
        assert content_decoded == {
            "qr_code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZoAAAGaAQAAAAAefbjOAAACGUlEQVR42u1cQXKEMAzzlAfkSXydJ/EAZrzEsZxAL21vHSkHDoAvRSNLsrfmvz+HqUhFKlKRilSkIhWhyPJs952Wj2z3a9x1P/HCHkVf9oejov9RZPj6/ZzbjY1242A/8+sPlPQHy3tCBAMiAgL9wx9FCv3eTRnXeBDYECL4EBEcccMisFHMIEQQc0S0jn1cQBQuRBDriNE6eq+wJh3Bi4jyGqCH10VegwwRr7P0D4OYWC2r/nokHJFUABxEMnFYqc1+ESJoOOJM2RjqIYUDegWsh7oGmbJMehii8rIkinEv7Yg4goYjkgAiioDdXBIqR0YhRNDoiBAJMJ4DFkM4VJ4dYw51DSodUb0CTcTsARXlEUw64hFX3ifMRXkNA3moa/DkEVf50MqlICuAFylLsjxitaBzU2K2E3UNLmXpFUTN4LJe0VyDz31CQEJeTocxe4p0BJWyLLvp6TmXuUZllkIEVR6BxZiKrZvXcLzibSGCiCNSJLQKtdu16ohDGzNUiFiibPfvXcNM7pMvoVrGXUkZOQNHJxEiyBAxOQI/1dh8agvNNbjc53t9aqpN4MC0ecvlNcbZasRZOHiaEHUNKmXp5yN28DnXmEG3EEHlPusXPA6igOHoR3kEKyIw5tgru66MW4hgRIQ9Xcdp63KVEEGnIx56MnpFLdlpz5LTa8y963U/wsURrHmE/h+LilSkIhWpSEUq+mnRB1XK9kLGEfa4AAAAAElFTkSuQmCC"
        }
