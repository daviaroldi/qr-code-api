import segno

from .base import QrCodeGenerator


class QrCodePhoneGenerator(QrCodeGenerator):
    @classmethod
    def generate(cls, body: dict) -> str:
        country_code = body.get("country_code")
        phone = body.get("phone")
        string_to_encode = "tel:+{}{}".format(country_code, phone)
        qr_code = segno.make(string_to_encode, micro=False)
        return qr_code.png_data_uri(scale=cls.scale)
