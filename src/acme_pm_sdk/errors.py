class AcmePMError(Exception):
    """Base exception for all SDK errors"""


class APIError(AcmePMError):
    def __init__(self, status_code: int, message: str, *, request_id: str | None = None):
        super().__init__(f"{status_code}: {message}")
        self.status_code = status_code
        self.message = message
        self.request_id = request_id


class AuthenticationError(APIError):
    pass


class NotFoundError(APIError):
    pass


class RateLimitError(APIError):
    pass
