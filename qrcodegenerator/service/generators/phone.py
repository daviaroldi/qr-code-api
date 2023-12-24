import segno


class PhoneQrCodeGenerator:
    @staticmethod
    def generate(country_code: str, phone: str) -> str:
        qr_code = segno.make("tel:+{}{}".format(country_code, phone))
        return qr_code.png_data_uri(scale=5)
