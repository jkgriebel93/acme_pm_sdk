from typing import Protocol, Mapping


class AuthProvider(Protocol):
    # TODO: Implement
    pass


class BearerAuth:
    def __init__(self, token: str):
        self.token = token

    def auth_headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.token}"}