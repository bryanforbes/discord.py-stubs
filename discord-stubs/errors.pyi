from typing import Any, Dict, Optional, Union

import aiohttp

class DiscordException(Exception): ...
class ClientException(DiscordException): ...
class NoMoreItems(DiscordException): ...
class GatewayNotFound(DiscordException): ...

def flatten_error_dict(d: Dict[str, Any], key: str = ...) -> Dict[str, Any]: ...

class HTTPException(DiscordException):
    response: aiohttp.ClientResponse
    text: str
    status: int
    code: int
    def __init__(
        self, response: aiohttp.ClientResponse, message: Union[str, Dict[str, Any]]
    ) -> None: ...

class Forbidden(HTTPException): ...
class NotFound(HTTPException): ...
class DiscordServerError(HTTPException): ...
class InvalidArgument(ClientException): ...
class LoginFailure(ClientException): ...

class ConnectionClosed(ClientException):
    code: Optional[int]
    reason: str
    shard_id: Optional[int]
    def __init__(
        self,
        socket: aiohttp.ClientWebSocketResponse,
        *,
        shard_id: Optional[int],
        code: Optional[int] = ...,
    ) -> None: ...

class PrivilegedIntentsRequired(ClientException):
    shard_id: Optional[int]
