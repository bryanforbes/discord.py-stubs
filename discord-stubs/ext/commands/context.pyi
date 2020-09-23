from typing import Any, Dict, List, Optional, TypeVar, Union

import discord

from .bot import Bot
from .cog import Cog
from .core import Command

_C = TypeVar('_C', bound=Context)

class Context(discord.abc.Messageable):
    message: discord.Message
    bot: Bot[Any]
    args: List[Any]
    kwargs: Dict[str, Any]
    prefix: str
    command: Command[Any]
    invoked_with: Optional[str]
    invoked_subcommand: Optional[Command[Any]]
    subcommand_passed: Optional[str]
    command_failed: bool
    async def invoke(
        self: _C, __command: Command[_C], *args: Any, **kwargs: Any
    ) -> Any: ...
    async def reinvoke(
        self, *, call_hooks: bool = ..., restart: bool = ...
    ) -> None: ...
    @property
    def valid(self) -> bool: ...
    @property
    def cog(self: _C) -> Optional[Cog[_C]]: ...
    @discord.utils.cached_property
    def guild(self) -> Optional[discord.Guild]: ...
    @discord.utils.cached_property
    def channel(
        self,
    ) -> Union[discord.TextChannel, discord.DMChannel, discord.GroupChannel]: ...
    @discord.utils.cached_property
    def author(self) -> Union[discord.User, discord.Member]: ...
    @discord.utils.cached_property
    def me(self) -> Union[discord.Member, discord.ClientUser]: ...
    @property
    def voice_client(self) -> Optional[discord.VoiceProtocol]: ...
    async def send_help(
        self: _C, __entity: Optional[Union[Command[_C], Cog[_C], str]]
    ) -> Any: ...
