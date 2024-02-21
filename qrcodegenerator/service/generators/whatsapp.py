import segno


class QrCodeWhatsappGenerator:
    @staticmethod
    def generate(body: dict) -> str:
        message = body.get("message")
        country_code = body.get("country_code")
        phone = body.get("phone")
        string_to_encode = "https://wa.me/{}{}".format(country_code, phone)
        if message:
            string_to_encode += "?text={}".format(message)
        qr_code = segno.make(string_to_encode, micro=False)
        return qr_code.png_data_uri(scale=5)
