from re import Match
from typing import Any, AnyStr, ClassVar, List, Optional, Pattern

import discord

from .bot import Bot
from .context import Context

class Converter:
    async def convert(self, ctx: Context, argument: str) -> Any: ...

class IDConverter(Converter):
    def _get_id_match(self, argument: Any) -> Match[AnyStr]: ...

class MemberConverter(IDConverter):
    async def query_member_named(
        self, guild: discord.Guild, argument: str
    ) -> Optional[discord.Member]: ...
    async def query_member_by_id(
        self, bot: Bot[Context], guild: discord.Guild, user_id: int
    ) -> Optional[discord.Member]: ...
    async def convert(self, ctx: Context, argument: str) -> discord.Member: ...

class UserConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.User: ...

class PartialMessageConverter(Converter):
    async def convert(self, ctx: Context, argument: str) -> discord.PartialMessage: ...

class MessageConverter(PartialMessageConverter):
    async def convert(  # type: ignore[override]
        self, ctx: Context, argument: str
    ) -> discord.Message: ...

class TextChannelConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.TextChannel: ...

class VoiceChannelConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.VoiceChannel: ...

class StageChannelConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.StageChannel: ...

class CategoryChannelConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.CategoryChannel: ...

class StoreChannelConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.StoreChannel: ...

class ColourConverter(Converter):
    RGB_REGEX: ClassVar[Pattern[str]]
    def parse_hex_number(self, argument: str) -> discord.Colour: ...
    def parse_rgb_number(self, argument: str, number: str) -> int: ...
    def parse_rgb(
        self, argument: str, *, regex: Pattern[str] = ...
    ) -> discord.Colour: ...
    async def convert(self, ctx: Context, argument: str) -> discord.Colour: ...

ColorConverter = ColourConverter

class RoleConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.Role: ...

class GameConverter(Converter):
    async def convert(self, ctx: Context, argument: str) -> discord.Game: ...

class InviteConverter(Converter):
    async def convert(self, ctx: Context, argument: str) -> discord.Invite: ...

class GuildConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.Guild: ...

class EmojiConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.Emoji: ...

class PartialEmojiConverter(Converter):
    async def convert(self, ctx: Context, argument: str) -> discord.PartialEmoji: ...

class clean_content(Converter):
    def __init__(
        self,
        *,
        fix_channel_mentions: bool = ...,
        use_nicknames: bool = ...,
        escape_markdown: bool = ...,
        remove_markdown: bool = ...,
    ) -> None: ...
    async def convert(self, ctx: Context, argument: str) -> str: ...

Greedy = List
