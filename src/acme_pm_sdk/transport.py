# This is the "transport" layer, meaning it handles HTTP operations.
# Another module I don't like the name of. Can't think of what other SDKs call it though.
import httpx
from typing import Any, Optional

DEFAULT_TIMEOUT = httpx.Timeout(connect=5.0, read=10.0, write=10.0, pool=5.0)

# TODO: Retry logic and richer transport will come later

class SyncTransport:
    def __init__(self, base_url: str, headers: dict[str, str], timeout: Optional[httpx.Timeout] = None):
        """

        Args:
            base_url:
            headers:
            timeout:
        """
        self._client = httpx.Client(base_url=base_url, headers=headers, timeout=timeout or DEFAULT_TIMEOUT)

    def request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:
        return self._client.request(method, url, **kwargs)


class AsyncTransport:
    def __init__(self, base_url: str, headers: dict[str,str], timeout: Optional[httpx.Timeout] = None):
        """

        Args:
            base_url:
            headers:
            timeout:
        """
        self._client = httpx.AsyncClient(base_url=base_url, headers=headers, timeout=timeout or DEFAULT_TIMEOUT)

    async def request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:
        """

        Args:
            method:
            url:
            **kwargs:

        Returns:

        """
        return await self._client.request(method, url, **kwargs)