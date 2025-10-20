from .auth import AuthProvider
from .transport import SyncTransport, AsyncTransport
from .services.projects import ProjectsAPI
from .services.tasks import TasksAPI
from .services.users import UsersAPI


class AcmePMClient:
    def __init__(self, base_url: str, auth: AuthProvider):
        """

        Args:
            base_url:
            auth:
        """
        self._transport = SyncTransport(base_url=base_url, headers=auth.auth_headers())
        self.projects = ProjectsAPI(self._transport)
        self.tasks = TasksAPI(self._transport)
        self.user = UsersAPI(self._transport)


class AsyncAcmePMClient:
    def __init__(self, base_url: str, auth: AuthProvider):
        """

        Args:
            base_url:
            auth:
        """
        self._transport = AsyncTransport(base_url, headers=auth.auth_headers())
        self.projects = ProjectsAPI(self._transport)
        self.tasks = TasksAPI(self._transport)
        self.users = UsersAPI(self._transport)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.aclose()

    async def aclose(self):
        await self._transport._client.aclose()
