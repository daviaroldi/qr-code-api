import json
import pytest


class TestQRCodePhoneGenerator:
    @pytest.mark.parametrize(
        "body,response",
        [
            (
                {"type": "whatsapp", "country_code": "55", "message": "Testing"},
                {"phone": "Required field"},
            ),
            (
                {"type": "whatsapp", "phone": "5199911223344", "message": "Testing"},
                {"country_code": "Required field"},
            ),
            (
                {"phone": "5199911223344", "country_code": "55", "message": "Testing"},
                {"type": "Required field"},
            ),
            (
                {"type": "whatsapp", "phone": "5199911223344", "country_code": "55"},
                {"message": "Required field"},
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
                {
                    "type": "whatsapp",
                    "country_code": "asdfe",
                    "phone": "5199911223344",
                    "message": "Testing message",
                },
                {"country_code": "Invalid value"},
            ),
            (
                {
                    "type": "whatsapp",
                    "country_code": False,
                    "phone": "5199911223344",
                    "message": "Testing message",
                },
                {"country_code": "Invalid value"},
            ),
            (
                {
                    "type": "whatsapp",
                    "country_code": None,
                    "phone": "5199911223344",
                    "message": "Testing message",
                },
                {"country_code": "Invalid value"},
            ),
            (
                {
                    "type": "whatsapp",
                    "country_code": "55",
                    "phone": "asdfeae",
                    "message": "Testing message",
                },
                {"phone": "Invalid value"},
            ),
            (
                {
                    "type": "whatsapp",
                    "country_code": "55",
                    "phone": False,
                    "message": "Testing message",
                },
                {"phone": "Invalid value"},
            ),
            (
                {
                    "type": "whatsapp",
                    "country_code": "55",
                    "phone": None,
                    "message": "Testing message",
                },
                {"phone": "Invalid value"},
            ),
            (
                {
                    "type": "whatsapp",
                    "country_code": "55",
                    "phone": "5199911223344",
                    "message": False,
                },
                {"message": "Invalid value"},
            ),
            (
                {
                    "type": "whatsapp",
                    "country_code": "55",
                    "phone": "5199911223344",
                    "message": None,
                },
                {"message": "Invalid value"},
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
        body = {
            "type": "whatsapp",
            "country_code": "55",
            "phone": "5199911223344",
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
            "qr_code": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXIAAAFyAQAAAADAX2ykAAABs0lEQVR42u2bTW6FMAyEo+YAHImrcyQOgJQXHDs2r908qVXl6MsCAZkVo/H4J5T20ToKePDgwYMHD/6X8EVX7W+2/rg3uVx997S9XfBf5bMF/n/xyq+Q187amd7k7t64H/d+CRD4TcrvLVPh8jB+I+elwu8a/Ip+PVzrO/hdRr9tuq76L/wu5b8apK+gX/w3Pb9vATleyJ/z8/tYMz6bdGM9xffMq1/VqhnuWD1SS7iG39T8iuE6lzPTOiw0E59z67dq1ev9jWNkzZdVwvCb139HV6PNrFlYdRETn9PXR0rt6D+HtUmXuqLf5PnzVUy1d2jebL6A/67kv3O+MKid7Q70m12/5yM0i4h1Q+7w3+T+e1rBO8JwqH/x3yXqX5vqyzv33+adSvjNrF8b6Ktgyw+VEvymro+szJ2ZtKXWqmT4zcxvTLJEv8GE93mcA36z1r/ftOoijokX3zNp/WuGO/1XI7Wd3yA+LxSf5/zXT8qi3+z5cyC0zPM5b+0O+M3P7/XMqa3dgX6X0a8XSf7/Avpdwn89l7KqiPnvWvlzuKth5g+/S9S//H8HHjx48ODB/z3+BUMcrsUWXneZAAAAAElFTkSuQmCC"
        }
