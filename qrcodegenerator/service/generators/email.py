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
        # qr_code = segno.make(
        #     "mailto:email@email.com?subject=Tracking%20for%20order%20%23141559&body=Tracking%20link%20for%20order%20%23141559%3A%0Ahttps%3A%2F%2Fm.ups.com",
        #     micro=False,
        # )
        qr_code = segno.make(string_to_encode, micro=False)
        return qr_code.png_data_uri(scale=cls.scale)
