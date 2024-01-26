import segno


class QrCodePhoneGenerator:
    @staticmethod
    def generate(body: dict) -> str:
        country_code = body.get("country_code")
        phone = body.get("phone")
        string_to_encode = "tel:+{}{}".format(country_code, phone)
        qr_code = segno.make(string_to_encode)
        return qr_code.png_data_uri(scale=5)
