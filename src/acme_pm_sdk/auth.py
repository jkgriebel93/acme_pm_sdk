from typing import Protocol, Mapping


class AuthProvider(Protocol):
    # TODO: Implement
    def auth_headers(self) -> Mapping[str, str]:
        """

        Returns:

        """
        return {}


class BearerAuth:
    def __init__(self, token: str):
        self.token = token

    def auth_headers(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.token}"}