import asyncio
import datetime
from typing import (
    Any,
    ClassVar,
    Coroutine,
    Dict,
    Generic,
    Iterable,
    Optional,
    TypeVar,
    Union,
    overload,
)
from typing_extensions import Literal

import aiohttp

from .abc import User as _ABCUser
from .asset import Asset
from .channel import TextChannel
from .embeds import Embed
from .enums import WebhookType
from .file import File
from .guild import Guild
from .http import _WebhookDict
from .mentions import AllowedMentions
from .message import Message
from .mixins import Hashable
from .state import ConnectionState

_T = TypeVar('_T')

_AsyncNone = Coroutine[Any, Any, None]
_AsyncOptionalMessage = Coroutine[Any, Any, Optional[WebhookMessage[_AsyncNone]]]

_N = TypeVar('_N', bound=Union[_AsyncNone, None])
_M = TypeVar('_M', bound=Union[_AsyncOptionalMessage, Optional[WebhookMessage[None]]])

class WebhookAdapter(Generic[_N, _M]):
    BASE: ClassVar[str]

    webhook: Webhook[_N, _M]
    def is_async(self) -> bool: ...
    def request(
        self,
        verb: str,
        url: str,
        payload: Optional[Dict[str, Any]] = ...,
        multipart: Optional[Dict[str, Any]] = ...,
    ) -> Any: ...
    def delete_webhook(self, *, reason: Optional[str] = ...) -> _N: ...
    def edit_webhook(
        self,
        *,
        reason: Optional[str] = ...,
        **payload: Any,
    ) -> _N: ...
    def edit_webhook_message(self, message_id: int, payload: Any) -> _N: ...
    def delete_webhook_message(self, message_id: int) -> _N: ...
    def handle_execution_response(
        self,
        response: Any,
        *,
        wait: bool,
    ) -> _M: ...
    def execute_webhook(
        self,
        *,
        payload: Dict[str, Any],
        wait: bool = ...,
        file: Optional[File] = ...,
        files: Optional[Iterable[File]] = ...,
    ) -> _M: ...

class AsyncWebhookAdapter(WebhookAdapter[_AsyncNone, _AsyncOptionalMessage]):
    session: aiohttp.ClientSession
    loop: asyncio.AbstractEventLoop
    def __init__(self, session: aiohttp.ClientSession) -> None: ...
    def is_async(self) -> bool: ...
    async def request(
        self,
        verb: str,
        url: str,
        payload: Optional[Dict[str, Any]] = ...,
        multipart: Optional[Dict[str, Any]] = ...,
        *,
        files: Optional[Iterable[File]] = ...,
        reason: Optional[str] = ...,
    ) -> Optional[WebhookMessage[_AsyncNone]]: ...

class RequestsWebhookAdapter(WebhookAdapter[None, WebhookMessage[None]]):
    session: Any
    def __init__(self, session: Optional[Any] = ..., *, sleep: bool = ...) -> None: ...
    def request(
        self,
        verb: str,
        url: str,
        payload: Optional[Dict[str, Any]] = ...,
        multipart: Optional[Dict[str, Any]] = ...,
        *,
        files: Optional[Iterable[File]] = ...,
        reason: Optional[str] = ...,
    ) -> WebhookMessage[None]: ...

class WebhookMessage(Message, Generic[_N]):
    @overload  # type: ignore[override]
    def edit(
        self,
        *,
        content: Optional[str] = ...,
        embed: Optional[Embed] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> _N: ...
    @overload
    def edit(
        self,
        *,
        content: Optional[str] = ...,
        embeds: Optional[Embed] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> _N: ...

class Webhook(Hashable, Generic[_N, _M]):
    id: int
    type: WebhookType
    token: Optional[str]
    channel_id: Optional[int]
    guild_id: Optional[int]
    name: Optional[str]
    avatar: Optional[str]
    user: Optional[_ABCUser]
    @property
    def url(self) -> str: ...
    @classmethod
    def partial(
        cls, id: int, token: str, *, adapter: WebhookAdapter[_N, _M]
    ) -> Webhook[_N, _M]: ...
    @classmethod
    def from_url(
        cls, url: str, *, adapter: WebhookAdapter[_N, _M]
    ) -> Webhook[_N, _M]: ...
    # NOTE: While this method is public, it should never be invoked by users.
    @classmethod
    def from_state(
        cls, data: _WebhookDict, state: ConnectionState
    ) -> _AsyncWebhook: ...
    @property
    def guild(self) -> Optional[Guild]: ...
    @property
    def channel(self) -> Optional[TextChannel]: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def avatar_url(self) -> Asset: ...
    def avatar_url_as(
        self, *, format: Optional[Literal['png', 'jpg', 'jpeg']] = ..., size: int = ...
    ) -> Asset: ...
    def delete(self, *, reason: Optional[str] = ...) -> _N: ...
    def edit(
        self,
        *,
        reason: Optional[str] = ...,
        name: Optional[str] = ...,
        avatar: Optional[bytes] = ...,
    ) -> _N: ...
    @overload
    def send(
        self,
        content: str,
        *,
        wait: bool = ...,
        username: Optional[str] = ...,
        avatar_url: Optional[Union[str, Asset]] = ...,
        tts: bool = ...,
        file: Optional[File] = ...,
        embed: Optional[Embed] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> _M: ...
    @overload
    def send(
        self,
        content: str,
        *,
        wait: bool = ...,
        username: Optional[str] = ...,
        avatar_url: Optional[Union[str, Asset]] = ...,
        tts: bool = ...,
        file: Optional[File] = ...,
        embeds: Optional[Iterable[Embed]] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> _M: ...
    @overload
    def send(
        self,
        content: str,
        *,
        wait: bool = ...,
        username: Optional[str] = ...,
        avatar_url: Optional[Union[str, Asset]] = ...,
        tts: bool = ...,
        files: Optional[Iterable[File]] = ...,
        embed: Optional[Embed] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> _M: ...
    @overload
    def send(
        self,
        content: str,
        *,
        wait: bool = ...,
        username: Optional[str] = ...,
        avatar_url: Optional[Union[str, Asset]] = ...,
        tts: bool = ...,
        files: Optional[Iterable[File]] = ...,
        embeds: Optional[Iterable[Embed]] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> _M: ...
    @overload
    def send(
        self,
        content: Optional[str] = ...,
        *,
        wait: bool = ...,
        username: Optional[str] = ...,
        avatar_url: Optional[Union[str, Asset]] = ...,
        tts: bool = ...,
        file: File,
        embed: Optional[Embed] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> _M: ...
    @overload
    def send(
        self,
        content: Optional[str] = ...,
        *,
        wait: bool = ...,
        username: Optional[str] = ...,
        avatar_url: Optional[Union[str, Asset]] = ...,
        tts: bool = ...,
        file: File,
        embeds: Optional[Iterable[Embed]] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> _M: ...
    @overload
    def send(
        self,
        content: Optional[str] = ...,
        *,
        wait: bool = ...,
        username: Optional[str] = ...,
        avatar_url: Optional[Union[str, Asset]] = ...,
        tts: bool = ...,
        files: Iterable[File],
        embed: Optional[Embed] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> _M: ...
    @overload
    def send(
        self,
        content: Optional[str] = ...,
        *,
        wait: bool = ...,
        username: Optional[str] = ...,
        avatar_url: Optional[Union[str, Asset]] = ...,
        tts: bool = ...,
        files: Iterable[File],
        embeds: Optional[Iterable[Embed]] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> _M: ...
    @overload
    def send(
        self,
        content: Optional[str] = ...,
        *,
        wait: bool = ...,
        username: Optional[str] = ...,
        avatar_url: Optional[Union[str, Asset]] = ...,
        tts: bool = ...,
        file: Optional[File] = ...,
        embed: Embed,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> _M: ...
    @overload
    def send(
        self,
        content: Optional[str] = ...,
        *,
        wait: bool = ...,
        username: Optional[str] = ...,
        avatar_url: Optional[Union[str, Asset]] = ...,
        tts: bool = ...,
        files: Optional[Iterable[File]] = ...,
        embed: Embed,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> _M: ...
    @overload
    def send(
        self,
        content: Optional[str] = ...,
        *,
        wait: bool = ...,
        username: Optional[str] = ...,
        avatar_url: Optional[Union[str, Asset]] = ...,
        tts: bool = ...,
        file: Optional[File] = ...,
        embeds: Iterable[Embed],
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> _M: ...
    @overload
    def send(
        self,
        content: Optional[str] = ...,
        *,
        wait: bool = ...,
        username: Optional[str] = ...,
        avatar_url: Optional[Union[str, Asset]] = ...,
        tts: bool = ...,
        files: Optional[Iterable[File]] = ...,
        embeds: Iterable[Embed],
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> _M: ...
    execute = send
    @overload
    def edit_message(
        self,
        message_id: int,
        *,
        content: Optional[str] = ...,
        embed: Optional[Embed] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> _N: ...
    @overload
    def edit_message(
        self,
        message_id: int,
        *,
        content: Optional[str] = ...,
        embeds: Optional[Embed] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> _N: ...
    def delete_message(self, message_id: int) -> _N: ...

_AsyncWebhook = Webhook[_AsyncNone, _AsyncOptionalMessage]
