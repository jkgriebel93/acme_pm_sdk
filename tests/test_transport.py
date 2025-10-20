import pytest
import respx
import httpx
from acme_pm_sdk.transport import SyncTransport, AsyncTransport
from acme_pm_sdk.errors import AuthenticationError

@respx.mock
def test_sync_raises_auth_error():
    respx.get("https://api.example.com/foo").mock(return_value=httpx.Response(401, json={
        "error": {"message": "Invalid token", "code": "unauthorized", "request_id": "xyz"}
    }))
    transport = SyncTransport("https://api.example.com", headers={})
    with pytest.raises(AuthenticationError):
        transport.request("GET", "/foo")

@pytest.mark.asyncio
@respx.mock
async def test_async_raises_auth_error():
    respx.get("https://api.example.com/foo").mock(return_value=httpx.Response(401, json={
        "error": {"message": "Invalid token", "code": "unauthorized", "request_id": "xyz"}
    }))
    transport = AsyncTransport("https://api.example.com", headers={})
    with pytest.raises(AuthenticationError):
        await transport.request("GET", "/foo")