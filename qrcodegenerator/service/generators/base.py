import segno


class QrCodeGenerator:
    scale = 10

    @classmethod
    def generate(cls, body: dict) -> str:
        string_to_encode = body["string_to_encode"]
        qr_code = segno.make(string_to_encode, micro=False)
        return qr_code.png_data_uri(scale=cls.scale)
