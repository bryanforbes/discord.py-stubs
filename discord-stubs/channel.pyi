import datetime
from typing import Callable, Dict, Iterable, List, Optional, Union, overload
from typing_extensions import Literal

import discord.abc

from .asset import _VALID_STATIC_ICON_FORMATS, Asset
from .enums import ChannelType, VoiceRegion
from .member import Member, VoiceState
from .message import Message, PartialMessage
from .mixins import Hashable
from .permissions import PermissionOverwrite, Permissions
from .role import Role
from .user import BaseUser, ClientUser, User
from .webhook import _AsyncWebhook

_OverwritesDict = Dict[Union[Role, Member], PermissionOverwrite]

class TextChannel(discord.abc.Messageable, discord.abc.GuildChannel, Hashable):
    topic: Optional[str]
    last_message_id: Optional[int]
    slowmode_delay: int
    nsfw: bool
    @property
    def type(self) -> Literal[ChannelType.text, ChannelType.news]: ...
    def permissions_for(self, member: Member) -> Permissions: ...
    @property
    def members(self) -> List[Member]: ...
    def is_nsfw(self) -> bool: ...
    def is_news(self) -> bool: ...
    @property
    def last_message(self) -> Optional[Message]: ...
    async def edit(
        self,
        *,
        reason: Optional[str] = ...,
        name: str = ...,
        topic: str = ...,
        position: int = ...,
        nsfw: bool = ...,
        sync_permissions: bool = ...,
        category: Optional[CategoryChannel] = ...,
        slowmode_delay: int = ...,
        type: ChannelType = ...,
        overwrites: _OverwritesDict = ...,
    ) -> None: ...
    async def delete_messages(self, messages: Iterable[Message]) -> None: ...
    async def purge(
        self,
        *,
        limit: Optional[int] = ...,
        check: Optional[Callable[[Message], bool]] = ...,
        before: Optional[Union[datetime.datetime, Message]] = ...,
        after: Optional[Union[datetime.datetime, Message]] = ...,
        around: Optional[Union[datetime.datetime, Message]] = ...,
        oldest_first: Optional[bool] = ...,
        bulk: bool = ...,
    ) -> List[Message]: ...
    async def webhooks(self) -> List[_AsyncWebhook]: ...
    async def create_webhook(
        self,
        *,
        name: str,
        avatar: Optional[Union[bytes, bytearray]] = ...,
        reason: Optional[str] = ...,
    ) -> _AsyncWebhook: ...
    async def follow(
        self, *, destination: TextChannel, reason: Optional[str] = ...
    ) -> _AsyncWebhook: ...
    def get_partial_message(self, message_id: int) -> PartialMessage: ...

class VocalGuildChannel(discord.abc.Connectable, discord.abc.GuildChannel, Hashable):
    bitrate: int
    user_limit: int
    rtc_region: Optional[VoiceRegion]
    @property
    def members(self) -> List[Member]: ...
    @property
    def voice_states(self) -> Dict[int, VoiceState]: ...
    def permissions_for(self, member: Member) -> Permissions: ...

class VoiceChannel(VocalGuildChannel):
    @property
    def type(self) -> Literal[ChannelType.voice]: ...
    async def edit(
        self,
        *,
        reason: Optional[str] = ...,
        name: str = ...,
        bitrate: int = ...,
        user_limit: int = ...,
        position: int = ...,
        sync_permissions: bool = ...,
        category: Optional[CategoryChannel] = ...,
        overwrites: _OverwritesDict = ...,
        rtc_region: Optional[VoiceRegion] = ...,
    ) -> None: ...

class StageChannel(VocalGuildChannel):
    topic: str
    @property
    def requesting_to_speak(self) -> List[Member]: ...
    @property
    def type(self) -> Literal[ChannelType.stage_voice]: ...
    async def edit(
        self,
        *,
        reason: Optional[str] = ...,
        name: str = ...,
        topic: str = ...,
        position: int = ...,
        sync_permissions: bool = ...,
        category: Optional[CategoryChannel] = ...,
        overwrites: _OverwritesDict = ...,
        rtc_region: Optional[VoiceRegion] = ...,
    ) -> None: ...

class CategoryChannel(discord.abc.GuildChannel, Hashable):
    nsfw: bool
    @property
    def type(self) -> Literal[ChannelType.category]: ...
    def is_nsfw(self) -> bool: ...
    async def edit(
        self,
        *,
        reason: Optional[str] = ...,
        name: str = ...,
        position: int = ...,
        nsfw: bool = ...,
        overwrites: Dict[Union[Role, Member], PermissionOverwrite] = ...,
    ) -> None: ...
    @overload
    async def move(
        self,
        *,
        beginning: bool,
        offset: int = ...,
        category: Optional[discord.abc.Snowflake] = ...,
        sync_permissions: bool = ...,
        reason: Optional[str] = ...,
    ) -> None: ...
    @overload
    async def move(
        self,
        *,
        end: bool,
        offset: int = ...,
        category: Optional[discord.abc.Snowflake] = ...,
        sync_permissions: bool = ...,
        reason: Optional[str] = ...,
    ) -> None: ...
    @overload
    async def move(
        self,
        *,
        before: discord.abc.Snowflake,
        offset: int = ...,
        category: Optional[discord.abc.Snowflake] = ...,
        sync_permissions: bool = ...,
        reason: Optional[str] = ...,
    ) -> None: ...
    @overload
    async def move(
        self,
        *,
        after: discord.abc.Snowflake,
        offset: int = ...,
        category: Optional[discord.abc.Snowflake] = ...,
        sync_permissions: bool = ...,
        reason: Optional[str] = ...,
    ) -> None: ...
    @property
    def channels(self) -> List[Union[TextChannel, VoiceChannel, StoreChannel]]: ...
    @property
    def text_channels(self) -> List[TextChannel]: ...
    @property
    def voice_channels(self) -> List[VoiceChannel]: ...
    @property
    def stage_channels(self) -> List[StageChannel]: ...
    async def create_text_channel(
        self,
        name: str,
        *,
        overwrites: Optional[Dict[Union[Role, Member], PermissionOverwrite]] = ...,
        position: int = ...,
        topic: str = ...,
        slowmode_delay: int = ...,
        nsfw: bool = ...,
        reason: Optional[str] = ...,
    ) -> TextChannel: ...
    async def create_voice_channel(
        self,
        name: str,
        *,
        overwrites: Optional[Dict[Union[Role, Member], PermissionOverwrite]] = ...,
        bitrate: int = ...,
        position: int = ...,
        user_limit: int = ...,
        rtc_region: Optional[VoiceRegion] = ...,
        reason: Optional[str] = ...,
    ) -> VoiceChannel: ...
    async def create_stage_channel(
        self,
        name: str,
        *,
        overwrites: Optional[Dict[Union[Role, Member], PermissionOverwrite]] = ...,
        topic: str = ...,
        position: int = ...,
        rtc_region: Optional[VoiceRegion] = ...,
        reason: Optional[str] = ...,
    ) -> StageChannel: ...

class StoreChannel(discord.abc.GuildChannel, Hashable):
    nsfw: bool
    @property
    def type(self) -> Literal[ChannelType.store]: ...
    def permissions_for(self, member: Member) -> Permissions: ...
    def is_nsfw(self) -> bool: ...
    async def edit(
        self,
        *,
        reason: Optional[str] = ...,
        name: str = ...,
        position: int = ...,
        nsfw: bool = ...,
        sync_permissions: bool = ...,
        category: Optional[CategoryChannel] = ...,
        overwrites: _OverwritesDict = ...,
    ) -> None: ...

class DMChannel(discord.abc.Messageable, Hashable):
    id: int
    recipient: User
    me: ClientUser
    @property
    def type(self) -> Literal[ChannelType.private]: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    def permissions_for(self, user: Optional[BaseUser] = ...) -> Permissions: ...
    def get_partial_message(self, message_id: int) -> PartialMessage: ...

class GroupChannel(discord.abc.Messageable, Hashable):
    id: int
    me: ClientUser
    owner: User
    icon: Optional[str]
    name: Optional[str]
    recipients: List[User]
    @property
    def type(self) -> Literal[ChannelType.group]: ...
    @property
    def icon_url(self) -> Asset: ...
    def icon_url_as(
        self, *, format: _VALID_STATIC_ICON_FORMATS = ..., size: int = ...
    ) -> Asset: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    def permissions_for(self, user: BaseUser) -> Permissions: ...
    async def add_recipients(self, *recipients: User) -> None: ...
    async def remove_recipients(self, *recipients: User) -> None: ...
    async def edit(
        self, name: Optional[str] = ..., icon: Optional[bytes] = ...
    ) -> None: ...
    async def leave(self) -> None: ...
