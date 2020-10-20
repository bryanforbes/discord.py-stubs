import datetime
from os import PathLike
from typing import BinaryIO, List, Optional, Union
from typing_extensions import TypedDict

from .abc import User as _BaseUser
from .calls import CallMessage
from .channel import DMChannel, GroupChannel, TextChannel
from .embeds import Embed
from .emoji import Emoji
from .enums import MessageType
from .file import File
from .flags import MessageFlags
from .guild import Guild
from .member import Member
from .mentions import AllowedMentions
from .mixins import Hashable
from .partial_emoji import PartialEmoji
from .reaction import Reaction
from .role import Role
from .user import ClientUser, User
from .utils import cached_slot_property

class Attachment:
    id: int
    size: int
    height: Optional[int]
    width: Optional[int]
    filename: str
    url: str
    proxy_url: str
    def is_spoiler(self) -> bool: ...
    async def save(
        self,
        fp: Union[BinaryIO, PathLike[str], str],
        *,
        seek_begin: bool = ...,
        use_cached: bool = ...,
    ) -> int: ...
    async def read(self, *, use_cached: bool = ...) -> bytes: ...
    async def to_file(self, *, use_cached: bool = ..., spoiler: bool = ...) -> File: ...

class MessageReference:
    message_id: Optional[int]
    channel_id: int
    guild_id: Optional[int]
    @property
    def cached_message(self) -> Optional[Message]: ...

class _MessageActivity(TypedDict, total=False):
    type: int
    party_id: str

class _MessageApplication(TypedDict):
    id: str
    name: str
    description: str
    icon: str
    cover_image: str

class Message(Hashable):
    id: int
    tts: bool
    type: MessageType
    author: Union[User, Member]
    content: str
    nonce: Union[int, str]
    embeds: List[Embed]
    channel: Union[TextChannel, DMChannel, GroupChannel]
    call: Optional[CallMessage]
    reference: Optional[MessageReference]
    mention_everyone: bool
    mentions: List[Union[User, Member, ClientUser]]
    role_mentions: List[Role]
    webhook_id: Optional[int]
    attachments: List[Attachment]
    pinned: bool
    flags: MessageFlags
    reactions: List[Reaction]
    activity: Optional[_MessageActivity]
    application: Optional[_MessageApplication]
    @cached_slot_property('_cs_guild')
    def guild(self) -> Optional[Guild]: ...
    @cached_slot_property('_cs_raw_mentions')
    def raw_mentions(self) -> List[int]: ...
    @cached_slot_property('_cs_raw_channel_mentions')
    def raw_channel_mentions(self) -> List[int]: ...
    @cached_slot_property('_cs_raw_role_mentions')
    def raw_role_mentions(self) -> List[int]: ...
    @cached_slot_property('_cs_channel_mentions')
    def channel_mentions(self) -> List[TextChannel]: ...
    @cached_slot_property('_cs_clean_content')
    def clean_content(self) -> str: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def edited_at(self) -> Optional[datetime.datetime]: ...
    @property
    def jump_url(self) -> str: ...
    def is_system(self) -> bool: ...
    @cached_slot_property('_cs_system_content')
    def system_content(self) -> str: ...
    async def delete(self, *, delay: Optional[float] = ...) -> None: ...
    async def edit(
        self,
        *,
        content: Optional[str] = ...,
        embed: Optional[Embed] = ...,
        suppress: bool = ...,
        delete_after: Optional[float] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
    ) -> None: ...
    async def publish(self) -> None: ...
    async def pin(self, *, reason: Optional[str] = ...) -> None: ...
    async def unpin(self, *, reason: Optional[str] = ...) -> None: ...
    async def add_reaction(
        self, emoji: Union[Emoji, Reaction, PartialEmoji, str]
    ) -> None: ...
    async def remove_reaction(
        self, emoji: Union[Emoji, Reaction, PartialEmoji, str], member: _BaseUser
    ) -> None: ...
    async def clear_reaction(
        self, emoji: Union[Emoji, Reaction, PartialEmoji, str]
    ) -> None: ...
    async def clear_reactions(self) -> None: ...
    async def ack(self) -> None: ...
