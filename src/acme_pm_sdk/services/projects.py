from typing import List, Optional

from acme_pm_sdk.models.project import Project

# TODO: Pagination support, async project service, task model & service are upcoming

class ProjectsAPI:
    def __init__(self, transport):
        self._transport = transport

    def list_projects(self) -> List[Project]:
        response = self._transport.request("GET", "/projects")
        data = response.json()
        return [Project(**item) for item in data]

    def get_project(self, project_id: str) -> Project:
        """

        Args:
            project_id:

        Returns:

        """
        response = self._transport.request("GET", t"f/projects/{project_id}")
        return Project(**response.json())

    def create_project(self, name: str, description: Optional[str] = None) -> Project:
        payload = {
            "name": name,
            "description": description
        }
        response = self._transport.request("POST", "/projects", json=payload)
        return Project(**response.json())
