import asyncio
from datetime import datetime
from typing import (
    Any,
    Callable,
    Coroutine,
    Iterator,
    List,
    Optional,
    Tuple,
    TypeVar,
    Union,
    overload,
)
from typing_extensions import Literal

import aiohttp

from .abc import Snowflake
from .activity import BaseActivity
from .appinfo import AppInfo
from .channel import (
    CategoryChannel,
    DMChannel,
    GroupChannel,
    StoreChannel,
    TextChannel,
    VoiceChannel,
)
from .emoji import Emoji
from .enums import Status, VoiceRegion
from .flags import Intents, MemberCacheFlags
from .gateway import DiscordWebSocket
from .guild import Guild
from .invite import Invite
from .iterators import GuildIterator
from .member import Member, VoiceState
from .mentions import AllowedMentions
from .message import Message
from .raw_models import (
    RawBulkMessageDeleteEvent,
    RawMessageDeleteEvent,
    RawMessageUpdateEvent,
    RawReactionActionEvent,
    RawReactionClearEmojiEvent,
    RawReactionClearEvent,
)
from .reaction import Reaction
from .relationship import Relationship
from .role import Role
from .template import Template
from .user import ClientUser, Profile, User
from .utils import SequenceProxy
from .voice_client import VoiceProtocol
from .webhook import Webhook
from .widget import Widget

_FuncType = Callable[..., Coroutine[Any, Any, Any]]
_F = TypeVar('_F', bound=_FuncType)
_GuildChannel = Union[TextChannel, VoiceChannel, CategoryChannel, StoreChannel]
_PrivateChannel = Union[DMChannel, GroupChannel]
_User = Union[User, Member]

class Client:
    ws: Optional[DiscordWebSocket]
    loop: asyncio.AbstractEventLoop
    shard_id: Optional[int]
    shard_count: Optional[int]
    activity: Optional[BaseActivity]
    allowed_mentions: Optional[AllowedMentions]
    def __init__(
        self,
        *,
        max_messages: Optional[int] = ...,
        loop: Optional[asyncio.AbstractEventLoop] = ...,
        connector: aiohttp.BaseConnector = ...,
        proxy: Optional[str] = ...,
        proxy_auth: Optional[aiohttp.BasicAuth] = ...,
        shard_id: Optional[int] = ...,
        shard_count: Optional[int] = ...,
        intents: Optional[Intents] = ...,
        member_cache_flags: Optional[MemberCacheFlags] = ...,
        fetch_offline_members: bool = ...,
        chunk_guilds_at_startup: bool = ...,
        status: Optional[Status] = ...,
        activity: Optional[BaseActivity] = ...,
        allowed_mentions: Optional[AllowedMentions] = ...,
        heartbeat_timeout: float = ...,
        guild_ready_timeout: float = ...,
        guild_subscriptions: bool = ...,
        assume_unsync_clock: bool = ...,
    ) -> None: ...
    @property
    def latency(self) -> float: ...
    # NOTE: user is actually Optional[ClientUser] because it's None when logged out, but the vast
    # majority of uses will be while logged in. Because of this fact, it is typed as ClientUser to
    # prevent false positives
    @property
    def user(self) -> ClientUser: ...
    @property
    def guilds(self) -> List[Guild]: ...
    @property
    def emojis(self) -> List[Emoji]: ...
    @property
    def cached_messages(self) -> SequenceProxy[Message]: ...
    @property
    def private_channels(self) -> List[_PrivateChannel]: ...
    @property
    def voice_clients(self) -> List[VoiceProtocol]: ...
    def is_ready(self) -> bool: ...
    def dispatch(self, __event: str, *args: Any, **kwargs: Any) -> None: ...
    async def on_error(self, event_method: str, *args: Any, **kwargs: Any) -> None: ...
    async def request_offline_members(self, *guilds: Guild) -> None: ...
    async def before_identify_hook(
        self, shard_id: int, *, initial: bool = ...
    ) -> None: ...
    async def login(self, token: str, *, bot: bool = ...) -> None: ...
    async def logout(self) -> None: ...
    async def connect(self, *, reconnect: bool = ...) -> None: ...
    async def close(self) -> None: ...
    def clear(self) -> None: ...
    async def start(
        self, token: str, *, bot: bool = ..., reconnect: bool = ...
    ) -> None: ...
    def run(self, token: str, *, bot: bool = ..., reconnect: bool = ...) -> None: ...
    def is_closed(self) -> bool: ...
    @property
    def intents(self) -> Intents: ...
    @property
    def users(self) -> List[User]: ...
    def get_channel(
        self, id: int
    ) -> Optional[Union[_GuildChannel, _PrivateChannel]]: ...
    def get_guild(self, id: int) -> Optional[Guild]: ...
    def get_user(self, id: int) -> Optional[User]: ...
    def get_emoji(self, id: int) -> Optional[Emoji]: ...
    def get_all_channels(self) -> Iterator[Union[_GuildChannel]]: ...
    def get_all_members(self) -> Iterator[Member]: ...
    async def wait_until_ready(self) -> None: ...
    @overload
    def wait_for(
        self,
        event: Literal['message'],
        *,
        check: Optional[Callable[[Message], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Message]: ...
    @overload
    def wait_for(
        self,
        event: Literal['message_delete'],
        *,
        check: Optional[Callable[[Message], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Message]: ...
    @overload
    def wait_for(
        self,
        event: Literal['bulk_message_delete'],
        *,
        check: Optional[Callable[[List[Message]], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[List[Message]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['raw_message_delete'],
        *,
        check: Optional[Callable[[RawMessageDeleteEvent], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[RawMessageDeleteEvent]: ...
    @overload
    def wait_for(
        self,
        event: Literal['raw_bulk_message_delete'],
        *,
        check: Optional[Callable[[RawBulkMessageDeleteEvent], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[RawBulkMessageDeleteEvent]: ...
    @overload
    def wait_for(
        self,
        event: Literal['message_edit'],
        *,
        check: Optional[Callable[[Message, Message], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[Message, Message]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['raw_message_edit'],
        *,
        check: Optional[Callable[[RawMessageUpdateEvent], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[RawMessageUpdateEvent]: ...
    @overload
    def wait_for(
        self,
        event: Literal['reaction_add'],
        *,
        check: Optional[Callable[[Reaction, Optional[_User]], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[Reaction, Optional[_User]]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['raw_reaction_add'],
        *,
        check: Optional[Callable[[RawReactionActionEvent], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[RawReactionActionEvent]: ...
    @overload
    def wait_for(
        self,
        event: Literal['reaction_remove'],
        *,
        check: Optional[Callable[[Reaction, Optional[_User]], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[Reaction, Optional[_User]]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['raw_reaction_remove'],
        *,
        check: Optional[Callable[[RawReactionActionEvent], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[RawReactionActionEvent]: ...
    @overload
    def wait_for(
        self,
        event: Literal['reaction_clear'],
        *,
        check: Optional[Callable[[Message, List[Reaction]], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[Message, List[Reaction]]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['raw_reaction_clear'],
        *,
        check: Optional[Callable[[RawReactionClearEvent], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[RawReactionClearEvent]: ...
    @overload
    def wait_for(
        self,
        event: Literal['reaction_clear_emoji'],
        *,
        check: Optional[Callable[[Reaction], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Reaction]: ...
    @overload
    def wait_for(
        self,
        event: Literal['raw_reaction_clear_emoji'],
        *,
        check: Optional[Callable[[RawReactionClearEmojiEvent], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[RawReactionClearEmojiEvent]: ...
    @overload
    def wait_for(
        self,
        event: Literal['private_channel_delete'],
        *,
        check: Optional[Callable[[_PrivateChannel], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[_PrivateChannel]: ...
    @overload
    def wait_for(
        self,
        event: Literal['private_channel_create'],
        *,
        check: Optional[Callable[[_PrivateChannel], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[_PrivateChannel]: ...
    @overload
    def wait_for(
        self,
        event: Literal['private_channel_update'],
        *,
        check: Optional[Callable[[_PrivateChannel, _PrivateChannel], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[_PrivateChannel, _PrivateChannel]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['private_channel_pins_update'],
        *,
        check: Optional[Callable[[_PrivateChannel, Optional[datetime]], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[_PrivateChannel, Optional[datetime]]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['guild_channel_delete'],
        *,
        check: Optional[Callable[[_GuildChannel], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[_GuildChannel]: ...
    @overload
    def wait_for(
        self,
        event: Literal['guild_channel_create'],
        *,
        check: Optional[Callable[[_GuildChannel], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[_GuildChannel]: ...
    @overload
    def wait_for(
        self,
        event: Literal['guild_channel_update'],
        *,
        check: Optional[Callable[[_GuildChannel, _GuildChannel], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[_GuildChannel, _GuildChannel]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['guild_channel_pins_update'],
        *,
        check: Optional[Callable[[_GuildChannel, Optional[datetime]], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[_GuildChannel, Optional[datetime]]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['guild_integrations_update'],
        *,
        check: Optional[Callable[[Guild], bool]],
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Guild]: ...
    @overload
    def wait_for(
        self,
        event: Literal['webhooks_update'],
        *,
        check: Optional[Callable[[_GuildChannel], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[_GuildChannel]: ...
    @overload
    def wait_for(
        self,
        event: Literal['member_join'],
        *,
        check: Optional[Callable[[Member], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Member]: ...
    @overload
    def wait_for(
        self,
        event: Literal['member_remove'],
        *,
        check: Optional[Callable[[Member], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Member]: ...
    @overload
    def wait_for(
        self,
        event: Literal['member_update'],
        *,
        check: Optional[Callable[[Member, Member], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[Member, Member]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['user_update'],
        *,
        check: Optional[Callable[[User, User], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[User, User]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['guild_join'],
        *,
        check: Optional[Callable[[Guild], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Guild]: ...
    @overload
    def wait_for(
        self,
        event: Literal['guild_remove'],
        *,
        check: Optional[Callable[[Guild], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Guild]: ...
    @overload
    def wait_for(
        self,
        event: Literal['guild_update'],
        *,
        check: Optional[Callable[[Guild, Guild], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[Guild, Guild]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['guild_role_create'],
        *,
        check: Optional[Callable[[Role], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Role]: ...
    @overload
    def wait_for(
        self,
        event: Literal['guild_role_delete'],
        *,
        check: Optional[Callable[[Role], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Role]: ...
    @overload
    def wait_for(
        self,
        event: Literal['guild_role_update'],
        *,
        check: Optional[Callable[[Role, Role], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[Role, Role]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['guild_emojis_update'],
        *,
        check: Optional[
            Callable[[Guild, Tuple[Emoji, ...], Tuple[Emoji, ...]], bool]
        ] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[Guild, Tuple[Emoji, ...], Tuple[Emoji, ...]]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['guild_available'],
        *,
        check: Optional[Callable[[Guild], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Guild]: ...
    @overload
    def wait_for(
        self,
        event: Literal['guild_unavailable'],
        *,
        check: Optional[Callable[[Guild], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Guild]: ...
    @overload
    def wait_for(
        self,
        event: Literal['voice_state_update'],
        *,
        check: Optional[Callable[[Member, VoiceState, VoiceState], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[Member, VoiceState, VoiceState]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['member_ban'],
        *,
        check: Optional[Callable[[Guild, _User], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[Guild, _User]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['member_unban'],
        *,
        check: Optional[Callable[[Guild, User], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[Guild, User]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['group_join'],
        *,
        check: Optional[Callable[[GroupChannel, User], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[GroupChannel, User]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['group_remove'],
        *,
        check: Optional[Callable[[GroupChannel, User], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[GroupChannel, User]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['relationship_add'],
        *,
        check: Optional[Callable[[Relationship], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Relationship]: ...
    @overload
    def wait_for(
        self,
        event: Literal['relationship_remove'],
        *,
        check: Optional[Callable[[Relationship], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Relationship]: ...
    @overload
    def wait_for(
        self,
        event: Literal['relationship_update'],
        *,
        check: Optional[Callable[[Relationship, Relationship], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Tuple[Relationship, Relationship]]: ...
    @overload
    def wait_for(
        self,
        event: Literal['invite_create'],
        *,
        check: Optional[Callable[[Invite], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Invite]: ...
    @overload
    def wait_for(
        self,
        event: Literal['invite_delete'],
        *,
        check: Optional[Callable[[Invite], bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Invite]: ...
    @overload
    def wait_for(
        self,
        event: str,
        *,
        check: Optional[Callable[..., bool]] = ...,
        timeout: Optional[float] = ...,
    ) -> asyncio.Future[Any]: ...
    def event(self, coro: _F) -> _F: ...
    async def change_presence(
        self,
        *,
        activity: Optional[BaseActivity] = ...,
        status: Optional[Status] = ...,
        afk: bool = ...,
    ) -> None: ...
    def fetch_guilds(
        self,
        *,
        limit: int = ...,
        before: Optional[Union[Snowflake, datetime]] = ...,
        after: Optional[Union[Snowflake, datetime]] = ...,
    ) -> GuildIterator: ...
    async def fetch_template(self, code: Union[str, Template]) -> Template: ...
    async def fetch_guild(self, guild_id: int) -> Guild: ...
    async def create_guild(
        self,
        name: str,
        region: Optional[VoiceRegion] = ...,
        icon: Optional[bytes] = ...,
        *,
        code: Optional[str] = ...,
    ) -> Guild: ...
    async def fetch_invite(
        self, url: Union[str, Invite], *, with_counts: bool = ...
    ) -> Invite: ...
    async def delete_invite(self, invite: Union[Invite, str]) -> None: ...
    async def fetch_widget(self, guild_id: int) -> Widget: ...
    async def application_info(self) -> AppInfo: ...
    async def fetch_user(self, user_id: int) -> User: ...
    async def fetch_user_profile(self, user_id: int) -> Profile: ...
    async def fetch_channel(
        self, channel_id: int
    ) -> Union[_GuildChannel, _PrivateChannel]: ...
    async def fetch_webhook(self, webhook_id: int) -> Webhook: ...
