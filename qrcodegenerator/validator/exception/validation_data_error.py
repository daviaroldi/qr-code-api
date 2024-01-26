class ValidationDataError(Exception):
    """
    Validation Data Error to provide error handling on validation data
    """

    message: any
    code: int

    def __init__(self, message, code=400):
        self.message = message
        self.code = code

        super().__init__(message, code)
