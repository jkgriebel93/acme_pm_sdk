from typing import List

from acme_pm_sdk.models.user import User


class UsersAPI:
    def __init__(self, transport):
        self._transport = transport


    def list_users(self) -> List[User]:
        response = self._transport.request("GET", "/users")
        return [User(**item) for item in response.json()]


    def get_user(self, user_id: str) -> User:
        response = self._transport.request("GET", f"/users/{user_id}")
        return User(**response.json())


class AsyncUsersAPI:
    def __init__(self, transport):
        self._transport = transport


    async def list_users(self) -> List[User]:
        response = await self._transport.request("GET", "/users")
        return [User(**item) for item in response.json()]
    
    
    async def get_user(self, user_id: str) -> User:
        response = await self._transport.request("GET", f"/users/{user_id}")
        return User(**response.json())