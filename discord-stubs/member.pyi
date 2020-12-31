import datetime
from typing import Any, List, Optional, Tuple, Union

import discord.abc

from .activity import BaseActivity, Spotify
from .channel import GroupChannel, VoiceChannel
from .colour import Colour
from .enums import Status
from .guild import Guild
from .message import Message
from .permissions import Permissions
from .role import Role
from .user import _CommonUser, _User

class VoiceState:
    deaf: bool
    mute: bool
    self_mute: bool
    self_deaf: bool
    self_stream: bool
    self_video: bool
    afk: bool
    channel: Optional[Union[GroupChannel, VoiceChannel]]
    session_id: str

class Member(_CommonUser, _User, discord.abc.Messageable, discord.abc.User):
    joined_at: Optional[datetime.datetime]
    activities: Tuple[Union[BaseActivity, Spotify], ...]
    nick: Optional[str]
    pending: bool
    premium_since: Optional[datetime.datetime]
    guild: Guild
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def status(self) -> Union[Status, str]: ...
    @property
    def raw_status(self) -> str: ...
    @property
    def mobile_status(self) -> Status: ...
    @property
    def desktop_status(self) -> Status: ...
    @property
    def web_status(self) -> Status: ...
    def is_on_mobile(self) -> bool: ...
    @property
    def colour(self) -> Colour: ...
    @property
    def color(self) -> Colour: ...
    @property
    def roles(self) -> List[Role]: ...
    @property
    def mention(self) -> str: ...
    @property
    def display_name(self) -> str: ...
    @property
    def activity(self) -> Union[BaseActivity, Spotify]: ...
    def mentioned_in(self, message: Message) -> bool: ...
    def permissions_in(self, channel: discord.abc.GuildChannel) -> Permissions: ...
    @property
    def top_role(self) -> Role: ...
    @property
    def guild_permissions(self) -> Permissions: ...
    @property
    def voice(self) -> Optional[VoiceState]: ...
    async def ban(
        self, *, reason: Optional[str] = ..., delete_message_days: int = ...
    ) -> None: ...
    async def unban(self, *, reason: Optional[str] = ...) -> None: ...
    async def kick(self, *, reason: Optional[str] = ...) -> None: ...
    async def edit(
        self,
        *,
        reason: Optional[str] = ...,
        nick: Optional[str] = ...,
        mute: bool = ...,
        deafen: bool = ...,
        roles: List[Role] = ...,
        voice_channel: Optional[VoiceChannel] = ...,
    ) -> None: ...
    async def move_to(
        self, channel: Optional[VoiceChannel], *, reason: Optional[str] = ...
    ) -> None: ...
    async def add_roles(
        self,
        *roles: discord.abc.Snowflake,
        reason: Optional[str] = ...,
        atomic: bool = ...,
    ) -> None: ...
    async def remove_roles(
        self,
        *roles: discord.abc.Snowflake,
        reason: Optional[str] = ...,
        atomic: bool = ...,
    ) -> None: ...
