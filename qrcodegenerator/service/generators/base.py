import segno


class QrCodeGenerator:
    @staticmethod
    def generate(string: str) -> str:
        qr_code = segno.make(string)
        return qr_code.png_data_uri(scale=5)
