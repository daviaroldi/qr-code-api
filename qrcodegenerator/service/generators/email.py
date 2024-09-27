import urllib.parse

import segno

from .base import QrCodeGenerator


class QrCodeEmailGenerator(QrCodeGenerator):
    @classmethod
    def generate(cls, body: dict) -> str:
        email = body.get("email")
        subject = body.get("subject")
        message = body.get("message")

        subject_and_message_encoded = urllib.parse.urlencode(
            {"subject": subject, "body": message}
        )

        string_to_encode = "mailto:{}?{}".format(email, subject_and_message_encoded)

        qr_code = segno.make(string_to_encode, micro=False)
        return qr_code.png_data_uri(scale=cls.scale)
