from typing import Optional, List

from acme_pm_sdk.models.task import Task


class TasksAPI:
    def __init__(self, transport):
        """

        Args:
            transport:

        Returns:

        """
        self._transport = transport

    def list_tasks(self, project_id: Optional[str] = None) -> List[Task]:
        """

        Args:
            project_id:

        Returns:

        """
        params = {"project_id": project_id} if project_id else {}
        response = self._transport.request("GET", "/tasks", params=params)
        return [Task(**item) for item in response.json()]

    def get_task(self, task_id: str) -> Task:
        response = self._transport.request("GET", f"/tasks/{task_id}")

        return Task(**response.json())

    def create_task(self, title: str, project_id: str, **kwargs) -> Task:
        payload = {"title": title, "project_id": project_id, **kwargs}

        response = self._transport.request("POST", "/tasks", json=payload)
        return Task(**response.json())

class AsyncTasksAPI:
    def __init__(self, transport):

        self._transport = transport

    async def list_tasks(self, project_id: Optional[str] = None) -> List[Task]:
        params = {"project_id": project_id} if project_id else {}

        response = await self._transport.request("GET", "/tasks", params=params)
        return [Task(**item) for item in response.json()]

    async def get_task(self, task_id: str) -> Task:
        response = await self._transport.request("GET", f"/tasks/{task_id}")

        return Task(**response.json())

    async def create_task(self, title: str, project_id: str, **kwargs) -> Task:
        payload = {"title": title, "project_id": project_id, **kwargs}

        response = await self._transport.request("POST", "/tasks", json=payload)
        return Task(**response.json())