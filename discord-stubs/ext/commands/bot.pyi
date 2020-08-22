import asyncio
from types import MappingProxyType, ModuleType
from typing import (
    Any,
    Callable,
    Coroutine,
    Dict,
    Iterable,
    List,
    Optional,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

import aiohttp

import discord

from .cog import Cog
from .context import Context
from .core import GroupMixin
from .help import HelpCommand

_CT = TypeVar('_CT', bound=Context)
_OT = TypeVar('_OT', bound=Context)

_CoroType = Callable[..., Coroutine[Any, Any, Any]]
_C = TypeVar('_C', bound=_CoroType)

_T = TypeVar('_T')
_CallablePrefix = Callable[[Bot, discord.Message], Union[_T, Coroutine[Any, Any, _T]]]
_CommandPrefix = Union[
    str, Iterable[str], _CallablePrefix[str], _CallablePrefix[Iterable[str]]
]

def when_mentioned(bot: Bot[Any], msg: discord.Message) -> List[str]: ...
def when_mentioned_or(
    *prefixes: str,
) -> Callable[[Bot[Any], discord.Message], List[str]]: ...

class BotBase(GroupMixin[_CT]):
    command_prefix: _CommandPrefix
    extra_events: Dict[str, List[Callable[..., Coroutine[Any, Any, None]]]]
    case_insensitive: bool
    description: str
    owner_id: Optional[int]
    owner_ids: Optional[Set[int]]
    help_command: Optional[HelpCommand[_CT]]
    def __init__(
        self,
        command_prefix: _CommandPrefix,
        help_command: Optional[HelpCommand[_CT]] = ...,
        description: Optional[str] = ...,
        **options: Any,
    ) -> None: ...
    def dispatch(self, __event_name: str, *args: Any, **kwargs: Any) -> None: ...
    async def close(self) -> None: ...
    async def on_command_error(self, context: _CT, exception: Exception) -> None: ...
    def check(self, func: _C) -> _C: ...
    def add_check(self, func: _CoroType, *, call_once: bool = ...) -> None: ...
    def remove_check(self, func: _CoroType, *, call_once: bool = ...) -> None: ...
    def check_once(self, func: _C) -> _C: ...
    async def can_run(self, ctx: _CT, *, call_once: bool = ...) -> None: ...
    async def is_owner(self, user: Union[discord.User, discord.Member]) -> bool: ...
    def before_invoke(self, coro: _C) -> _C: ...
    def after_invoke(self, coro: _C) -> _C: ...
    def add_listener(self, func: _CoroType, name: Optional[str] = ...) -> None: ...
    def remove_listener(self, func: _CoroType, name: Optional[str] = ...) -> None: ...
    def listen(self, name: Optional[str] = ...) -> Callable[[_C], _C]: ...
    def add_cog(self, cog: Cog[_CT]) -> None: ...
    def get_cog(self, name: str) -> Cog[_CT]: ...
    def remove_cog(self, name: str) -> None: ...
    @property
    def cogs(self) -> MappingProxyType[str, Cog[_CT]]: ...
    def load_extension(self, name: str) -> None: ...
    def unload_extension(self, name: str) -> None: ...
    def reload_extension(self, name: str) -> None: ...
    @property
    def extensions(self) -> MappingProxyType[str, ModuleType]: ...
    async def get_prefix(self, message: discord.Message) -> Union[List[str], str]: ...
    @overload
    async def get_context(self, message: discord.Message) -> _CT: ...
    @overload
    async def get_context(self, message: discord.Message, *, cls: Type[_OT]) -> _OT: ...
    async def invoke(self, ctx: _CT) -> None: ...
    async def process_commands(self, message: discord.Message) -> None: ...
    @overload
    async def process_commands(self, message: discord.Message, cls=Context) -> None: ...
    async def on_message(self, message: discord.Message) -> None: ...

class Bot(BotBase[_CT], discord.Client):
    def __new__(
        self,
        command_prefix: _CommandPrefix,
        help_command: Optional[HelpCommand[Context]] = ...,
        description: Optional[str] = ...,
        *,
        case_insensitive: bool = ...,
        loop: Optional[asyncio.AbstractEventLoop] = ...,
        shard_id: Optional[int] = ...,
        shard_count: Optional[int] = ...,
        connector: aiohttp.BaseConnector = ...,
        proxy: Optional[str] = ...,
        proxy_auth: Optional[aiohttp.BasicAuth] = ...,
        max_messages: Optional[int] = ...,
        fetch_offline_members: bool = ...,
        status: Optional[discord.Status] = ...,
        activity: Optional[
            Union[discord.Activity, discord.Game, discord.Streaming]
        ] = ...,
        heartbeat_timeout: float = ...,
        **options: Any,
    ) -> Bot[Context]: ...

class AutoShardedBot(BotBase[_CT], discord.AutoShardedClient):
    def __new__(
        self,
        command_prefix: _CommandPrefix,
        help_command: HelpCommand[Context],
        description: Optional[str] = ...,
        *,
        case_insensitive: bool = ...,
        loop: Optional[asyncio.AbstractEventLoop] = ...,
        shard_ids: Optional[Union[List[int], Tuple[int]]] = ...,
        shard_count: Optional[int] = ...,
        connector: aiohttp.BaseConnector = ...,
        proxy: Optional[str] = ...,
        proxy_auth: Optional[aiohttp.BasicAuth] = ...,
        max_messages: Optional[int] = ...,
        fetch_offline_members: bool = ...,
        status: Optional[discord.Status] = ...,
        activity: Optional[
            Union[discord.Activity, discord.Game, discord.Streaming]
        ] = ...,
        heartbeat_timeout: float = ...,
        **options: Any,
    ) -> AutoShardedBot[Context]: ...
