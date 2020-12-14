import asyncio
import datetime
from typing import (
    Any,
    BinaryIO,
    ClassVar,
    Coroutine,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Type,
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

class WebhookAdapter:
    BASE: ClassVar[str] = ...

    webhook: Webhook
    def is_async(self) -> bool: ...
    def request(
        self,
        verb: str,
        url: str,
        payload: Optional[Dict[str, Any]] = ...,
        multipart: Optional[Dict[str, Any]] = ...,
    ) -> Any: ...
    def delete_webhook(self, *, reason: Optional[str] = ...) -> Any: ...
    def edit_webhook(self, *, reason: Optional[str] = ..., **payload: Any) -> Any: ...
    def edit_webhook_message(self, message_id: int, payload: Any) -> Any: ...
    def delete_webhook_message(self, message_id: int) -> Any: ...
    def handle_execution_response(self, data: Any, *, wait: bool) -> Any: ...
    def execute_webhook(
        self,
        *,
        payload: Dict[str, Any],
        wait: bool = ...,
        file: Optional[Tuple[str, BinaryIO, str]] = ...,
        files: Optional[List[Tuple[str, BinaryIO, str]]] = ...,
    ) -> Any: ...

class AsyncWebhookAdapter(WebhookAdapter):
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
    ) -> Any: ...
    @overload
    async def handle_execution_response(
        self, response: Any, *, wait: Literal[True]
    ) -> WebhookMessage: ...
    @overload
    async def handle_execution_response(
        self, response: Coroutine[Any, Any, _T], *, wait: Literal[False]
    ) -> _T: ...
    @overload
    async def handle_execution_response(
        self, response: Coroutine[Any, Any, _T], *, wait: bool
    ) -> Union[_T, WebhookMessage]: ...

class RequestsWebhookAdapter(WebhookAdapter):
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
    ) -> Any: ...
    @overload
    def handle_execution_response(
        self, response: Any, *, wait: Literal[True]
    ) -> WebhookMessage: ...
    @overload
    def handle_execution_response(
        self, response: _T, *, wait: Literal[False]
    ) -> _T: ...
    @overload
    def handle_execution_response(
        self, response: _T, *, wait: bool
    ) -> Union[_T, WebhookMessage]: ...

class WebhookMessage(Message):
    @overload  # type: ignore[override]
    def edit(
        self,
        *,
        content: Optional[str] = ...,
        embed: Optional[Embed] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> Union[None, Coroutine[Any, Any, None]]: ...
    @overload
    def edit(
        self,
        *,
        content: Optional[str] = ...,
        embeds: Optional[Embed] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> Union[None, Coroutine[Any, Any, None]]: ...

_W = TypeVar('_W', bound=Webhook)

class Webhook(Hashable):
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
        cls: Type[_W], id: int, token: str, *, adapter: WebhookAdapter
    ) -> _W: ...
    @classmethod
    def from_url(cls: Type[_W], url: str, *, adapter: WebhookAdapter) -> _W: ...
    # NOTE: While this method is public, it should never be invoked by users.
    @classmethod
    def from_state(cls: Type[_W], data: _WebhookDict, state: ConnectionState) -> _W: ...
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
    def delete(
        self, *, reason: Optional[str] = ...
    ) -> Union[None, Coroutine[Any, Any, None]]: ...
    def edit(
        self,
        *,
        reason: Optional[str] = ...,
        name: Optional[str] = ...,
        avatar: Optional[bytes] = ...,
    ) -> Union[_WebhookDict, Coroutine[Any, Any, _WebhookDict]]: ...
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
        embed: Optional[Embed] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> Union[WebhookMessage, Coroutine[Any, Any, WebhookMessage]]: ...
    @overload
    def send(
        self,
        content: Optional[str] = ...,
        *,
        wait: bool = ...,
        username: Optional[str] = ...,
        avatar_url: Optional[Union[str, Asset]] = ...,
        tts: bool = ...,
        files: Optional[List[File]] = ...,
        embed: Optional[Embed] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> Union[WebhookMessage, Coroutine[Any, Any, WebhookMessage]]: ...
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
        embeds: Optional[List[Embed]] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> Union[WebhookMessage, Coroutine[Any, Any, WebhookMessage]]: ...
    @overload
    def send(
        self,
        content: Optional[str] = ...,
        *,
        wait: bool = ...,
        username: Optional[str] = ...,
        avatar_url: Optional[Union[str, Asset]] = ...,
        tts: bool = ...,
        files: Optional[List[File]] = ...,
        embeds: Optional[List[Embed]] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> Union[WebhookMessage, Coroutine[Any, Any, WebhookMessage]]: ...
    def execute(self, *args: Any, **kwargs: Any) -> Any: ...
    @overload
    def edit_message(
        self,
        message_id: int,
        *,
        content: Optional[str] = ...,
        embed: Optional[Embed] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> Union[None, Coroutine[Any, Any, None]]: ...
    @overload
    def edit_message(
        self,
        message_id: int,
        *,
        content: Optional[str] = ...,
        embeds: Optional[Embed] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> Union[None, Coroutine[Any, Any, None]]: ...
    def delete_message(
        self, message_id: int
    ) -> Union[None, Coroutine[Any, Any, None]]: ...
