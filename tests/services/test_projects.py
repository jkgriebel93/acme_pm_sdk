# tests/services/test_projects.py

import pytest
import respx
import httpx

from acme_pm_sdk.client import AcmePMClient
from acme_pm_sdk.auth import BearerAuth
from acme_pm_sdk.services.projects import ProjectsAPI
from acme_pm_sdk.models.project import Project


@pytest.fixture
def client() -> AcmePMClient:
    return AcmePMClient(base_url="https://api.example.com",
                        auth=BearerAuth(token="foo"))


@respx.mock
def test_get_project(client: AcmePMClient):
    mock = respx.get("https://api.example.com/projects/abc123").mock(
        return_value=httpx.Response(
            200,
            json={"id": "abc123", "name": "Example Project"},
        )
    )

    project = client.projects.get_project("abc123")
    assert isinstance(project, Project)
    assert project.id == "abc123"
    assert project.name == "Example Project"
    assert mock.called


# Async version
@pytest.mark.asyncio
@respx.mock
async def test_async_get_project():
    from acme_pm_sdk.client import AsyncAcmePMClient

    respx.get("https://api.example.com/projects/xyz456").mock(
        return_value=httpx.Response(
            200,
            json={"id": "xyz456", "name": "Async Project"},
        )
    )

    async with AsyncAcmePMClient(base_url="https://api.example.com",
                                 auth=BearerAuth(token="foot")) as client:
        project = await client.projects.get_project("xyz456")

    assert isinstance(project, Project)
    assert project.id == "xyz456"
    assert project.name == "Async Project"
