# This is the "transport" layer, meaning it handles HTTP operations.
# Another module I don't like the name of. Can't think of what other SDKs call it though.
import httpx
from typing import Any, Optional, Mapping

from acme_pm_sdk.errors import APIError, AuthenticationError, NotFoundError, RateLimitError

DEFAULT_TIMEOUT = httpx.Timeout(connect=5.0, read=10.0, write=10.0, pool=5.0)


def raise_for_status(response: httpx.Response):
    if 200 <= response.status_code < 300:
        return

    try:
        error = response.json().get("error", {})
        message = error.get("message", response.text)
        code = error.get("code")
        request_id = error.get("request_id")
    except Exception:
        message = response.text
        code = None
        request_id = None

    if response.status_code == 401 or code == "unauthorized":
        raise AuthenticationError(response.status_code, message, request_id=request_id)
    elif response.status_code == 404 or code == "not_found":
        raise NotFoundError(response.status_code, message, request_id=request_id)
    elif response.status_code == 429 or code == "rate_limited":
        raise RateLimitError(response.status_code, message, request_id=request_id)
    else:
        raise APIError(response.status_code, message, request_id=request_id)


class SyncTransport:
    def __init__(self, base_url: str, headers: Mapping[str, str], timeout: Optional[httpx.Timeout] = None):
        """

        Args:
            base_url:
            headers:
            timeout:
        """
        self._client = httpx.Client(base_url=base_url, headers=headers, timeout=timeout or DEFAULT_TIMEOUT)

    def request(self, method: str, url: str, **kwargs: Any) -> httpx.Response:
        response = self._client.request(method, url, **kwargs)
        raise_for_status(response)
        return response


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
        response = await self._client.request(method, url, **kwargs)
        raise_for_status(response)
        return response