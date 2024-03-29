import asyncio
import threading
from typing import (
    Any,
    Callable,
    ClassVar,
    Dict,
    Iterable,
    List,
    NamedTuple,
    Optional,
    Type,
    TypeVar,
    Union,
    type_check_only,
)
from typing_extensions import Literal, TypedDict

import aiohttp

from .activity import BaseActivity
from .client import Client
from .enums import SpeakingState
from .voice_client import VoiceClient

@type_check_only
class _KeepAlivePayloadDict(TypedDict):
    op: int
    d: int

class ReconnectWebSocket(Exception):
    shard_id: int
    resume: bool
    op: Literal['RESUME', 'IDENTIFY']
    def __init__(self, shard_id: int, *, resume: bool = ...) -> None: ...

class WebSocketClosure(Exception): ...

class EventListener(NamedTuple):
    predicate: Callable[[Any], bool]
    event: str
    result: Optional[Callable[[Any], Any]]
    future: asyncio.Future[Any]

class GatewayRatelimiter:
    def __init__(self, count: int = ..., per: float = ...) -> None: ...
    def get_delay(self) -> float: ...
    def is_ratelimited(self) -> bool: ...
    async def block(self) -> None: ...

class KeepAliveHandler(threading.Thread):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def run(self) -> None: ...
    def get_payload(self) -> _KeepAlivePayloadDict: ...
    def stop(self) -> None: ...
    def tick(self) -> None: ...
    def ack(self) -> None: ...

class VoiceKeepAliveHandler(KeepAliveHandler): ...

_DWS = TypeVar('_DWS', bound=DiscordWebSocket)

class DiscordClientWebSocketResponse(aiohttp.ClientWebSocketResponse):
    async def close(self, *, code: int = ..., message: bytes = ...) -> bool: ...

class DiscordWebSocket:
    DISPATCH: ClassVar[int]
    HEARTBEAT: ClassVar[int]
    IDENTIFY: ClassVar[int]
    PRESENCE: ClassVar[int]
    VOICE_STATE: ClassVar[int]
    VOICE_PING: ClassVar[int]
    RESUME: ClassVar[int]
    RECONNECT: ClassVar[int]
    REQUEST_MEMBERS: ClassVar[int]
    INVALIDATE_SESSION: ClassVar[int]
    HELLO: ClassVar[int]
    HEARTBEAT_ACK: ClassVar[int]
    GUILD_SYNC: ClassVar[int]

    thread_id: int
    session_id: Optional[int]
    sequence: Optional[int]
    @property
    def open(self) -> bool: ...
    def is_ratelimited(self) -> bool: ...
    @classmethod
    async def from_client(
        cls: Type[_DWS],
        client: Client,
        *,
        initial: bool = ...,
        gateway: Optional[str] = ...,
        shard_id: Optional[int] = ...,
        session: Optional[int] = ...,
        sequence: Optional[int] = ...,
        resume: bool = ...,
    ) -> _DWS: ...
    def wait_for(
        self,
        event: str,
        predicate: Callable[[Any], bool],
        result: Optional[Callable[[Any], Any]] = ...,
    ) -> asyncio.Future[Any]: ...
    async def identify(self) -> None: ...
    async def resume(self) -> None: ...
    async def received_message(self, msg: Union[str, bytes]) -> None: ...
    @property
    def latency(self) -> float: ...
    async def poll_event(self) -> None: ...
    async def send(self, data: str) -> None: ...
    async def send_as_json(self, data: Any) -> None: ...
    async def send_heartbeat(self, data: Any) -> None: ...
    async def change_presence(
        self,
        *,
        activity: Optional[BaseActivity] = ...,
        status: Optional[str] = ...,
        afk: bool = ...,
        since: float = ...,
    ) -> None: ...
    async def request_sync(self, guild_ids: Iterable[int]) -> None: ...
    async def request_chunks(
        self,
        guild_id: int,
        query: Optional[str] = ...,
        *,
        limit: int,
        user_ids: Optional[List[int]] = ...,
        presences: bool = ...,
        nonce: Optional[str] = ...,
    ) -> None: ...
    async def voice_state(
        self,
        guild_id: int,
        channel_id: Optional[int],
        self_mute: bool = ...,
        self_deaf: bool = ...,
    ) -> None: ...
    async def close(self, code: int = ...) -> None: ...

_DVWS = TypeVar('_DVWS', bound=DiscordVoiceWebSocket)

class DiscordVoiceWebSocket:
    IDENTIFY: ClassVar[int]
    SELECT_PROTOCOL: ClassVar[int]
    READY: ClassVar[int]
    HEARTBEAT: ClassVar[int]
    SESSION_DESCRIPTION: ClassVar[int]
    SPEAKING: ClassVar[int]
    HEARTBEAT_ACK: ClassVar[int]
    RESUME: ClassVar[int]
    HELLO: ClassVar[int]
    RESUMED: ClassVar[int]
    CLIENT_CONNECT: ClassVar[int]
    CLIENT_DISCONNECT: ClassVar[int]

    thread_id: int
    async def send_as_json(self, data: Any) -> None: ...
    async def send_heartbeat(self, data: Any) -> None: ...
    async def resume(self) -> None: ...
    async def identify(self) -> None: ...
    @classmethod
    async def from_client(
        cls: Type[_DVWS], client: VoiceClient, *, resume: bool = ...
    ) -> _DVWS: ...
    async def select_protocol(self, ip: str, port: str, mode: str) -> None: ...
    async def client_connect(self) -> None: ...
    async def speak(self, state: SpeakingState = ...) -> None: ...
    async def received_message(self, msg: Dict[str, Any]) -> None: ...
    async def initial_connection(self, data: Dict[str, Any]) -> None: ...
    @property
    def latency(self) -> float: ...
    @property
    def average_latency(self) -> float: ...
    async def load_secret_key(self, data: Dict[str, Any]) -> None: ...
    async def poll_event(self) -> None: ...
    async def close(self, code: int = ...) -> None: ...
