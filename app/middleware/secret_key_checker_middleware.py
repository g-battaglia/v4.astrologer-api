"""
    This is part of Astrologer API (C) 2023 Giacomo Battaglia
"""

from starlette.datastructures import URL, Headers
from starlette.responses import JSONResponse, RedirectResponse, Response
from starlette.types import ASGIApp, Receive, Scope, Send


class SecretKeyCheckerMiddleware:
    def __init__(self, app: ASGIApp, secret_key_name: str, secret_keys: list = []) -> None:
        self.app = app
        self.allowed_hosts = list(secret_keys)
        self.secret_key_name = secret_key_name

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        headers = Headers(scope=scope)
        host = headers.get(self.secret_key_name, "").split(":")[0]
        is_valid_key = False

        for key in self.allowed_hosts:
            if host == key:
                is_valid_key = True
                break

        if is_valid_key:
            await self.app(scope, receive, send)

        else:
            response = JSONResponse(status_code=400, content={"status": "KO", "message": "Bad request"})

            await response(scope, receive, send)
