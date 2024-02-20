import segno


class QrCodeGenerator:
    @staticmethod
    def generate(body: dict) -> str:
        string_to_encode = body["string_to_encode"]
        qr_code = segno.make(string_to_encode, micro=False)
        return qr_code.png_data_uri(scale=10)
