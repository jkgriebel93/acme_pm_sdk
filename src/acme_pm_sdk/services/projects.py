from typing import List, Optional, AsyncIterator

from acme_pm_sdk.models.project import Project
from ..pagination import PageIterator

# TODO: Retries and error mapping

class ProjectsAPI:
    def __init__(self, transport):
        self._transport = transport

    def list_page(self, page: int = 1, page_size: int = 50) -> List[Project]:
        """

        Args:
            page:
            page_size:

        Returns:

        """
        response = self._transport.request("GET",
                                           "/projects",
                                           params={"page": page,
                                                   "limit": page_size})
        return [Project(**item) for item in response.json()]

    def iter_all(self, page_size: int = 50) -> PageIterator[Project]:
        return PageIterator(lambda page: self.list_page(page, page_size=page_size))

    def list_projects(self, page_size: int = 50) -> List[Project]:
        """

        Args:
            page_size:

        Returns:

        """
        # TODO: This pagination implementation can
        #  be generalized so it can be used elsewhere
        projects = []
        page = 1
        while True:
            response = self._transport.request("GET",
                                               "/projects",
                                               params={"page": page, "limit": page_size})
            data = response.json()["data"]
            items = [Project(**item) for item in data]

            if not items:
                break

            projects.extend(items)
            page += 1

        return projects

    def get_project(self, project_id: str) -> Project:
        """

        Args:
            project_id:

        Returns:

        """
        response = self._transport.request("GET", f"/projects/{project_id}")
        return Project(**response.json())

    def create_project(self, name: str, description: Optional[str] = None) -> Project:
        """

        Args:
            name:
            description:

        Returns:

        """
        payload = {
            "name": name,
            "description": description
        }
        response = self._transport.request("POST", "/projects", json=payload)
        return Project(**response.json())


class AsyncProjectsAPI:
    def __init__(self, transport):
        self._transport = transport

    async def list_page(self, page: int = 1, page_size: int = 50) -> List[Project]:
        response = await self._transport.request("GET",
                                                 "/projects",
                                                 params={"page": page,
                                                         "limit": page_size})
        return [Project(**item) for item in response.json()]

    async def iter_all(self, page_size: int = 50) -> AsyncIterator[Project]:
        page = 1
        while True:
            items = await self.list_page(page=page, page_size=page_size)
            if not items:
                break

            for item in items:
                yield item
            page += 1

    async def list_projects(self, page_size: int = 50) -> List[Project]:
        """

        Args:
            page_size:

        Returns:

        """
        projects = []
        page = 1
        while True:
            response = await self._transport.request("GET",
                                                     "/projects",
                                                     params={"page": page, "limit": page_size})
            data = response.json()
            items = [Project(**item) for item in data]

            if not items:
                break

            projects.extend(items)
            page += 1

        return projects

    async def get_project(self, project_id: str) -> Project:
        """

        Args:
            project_id:

        Returns:

        """
        response = await self._transport.request("GET",
                                                 f"/projects/{project_id}")
        return Project(**response.json())

    async def create_project(self, name: str, description: Optional[str] = None) -> Project:
        """

        Args:
            name:
            description:

        Returns:

        """
        payload = {
            "name": name,
            "description": description
        }
        response = await self._transport.request("POST",
                                                 "/projects",
                                                 json=payload)
        return Project(**response.json())