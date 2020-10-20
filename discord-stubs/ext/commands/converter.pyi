from typing import Any, List, Optional

import discord

from .bot import Bot
from .context import Context

class Converter:
    async def convert(self, ctx: Context, argument: str) -> Any: ...

class IDConverter(Converter): ...

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

class MessageConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.Message: ...

class TextChannelConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.TextChannel: ...

class VoiceChannelConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.VoiceChannel: ...

class CategoryChannelConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.CategoryChannel: ...

class ColourConverter(Converter):
    async def convert(self, ctx: Context, argument: str) -> discord.Colour: ...

ColorConverter = ColourConverter

class RoleConverter(IDConverter):
    async def convert(self, ctx: Context, argument: str) -> discord.Role: ...

class GameConverter(Converter):
    async def convert(self, ctx: Context, argument: str) -> discord.Game: ...

class InviteConverter(Converter):
    async def convert(self, ctx: Context, argument: str) -> discord.Invite: ...

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
    ) -> None: ...
    async def convert(self, ctx: Context, argument: str) -> str: ...

Greedy = List
