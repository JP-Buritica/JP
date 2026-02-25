from dataclasses import dataclass

import httpx
from httpx import HTTPError

from app.config import settings


class IntegrationError(Exception):
    """Raised when an external dependency is unavailable."""


@dataclass
class UsersRoutesValidator:
    users_base_url: str = settings.users_service_url
    routes_base_url: str = settings.routes_service_url
    timeout: float = settings.external_request_timeout

    async def user_exists(self, user_id: str) -> bool:
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(f"{self.users_base_url}/users/{user_id}")
        except HTTPError as exc:
            raise IntegrationError("Users service unavailable") from exc
        if response.status_code == 200:
            return True
        if response.status_code == 404:
            return False
        raise IntegrationError("Users service unavailable")

    async def route_exists(self, route_id: str) -> bool:
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(f"{self.routes_base_url}/routes/{route_id}")
        except HTTPError as exc:
            raise IntegrationError("Routes service unavailable") from exc
        if response.status_code == 200:
            return True
        if response.status_code == 404:
            return False
        raise IntegrationError("Routes service unavailable")
