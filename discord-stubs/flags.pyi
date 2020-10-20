from typing import (
    Any,
    Callable,
    ClassVar,
    Dict,
    Iterator,
    List,
    Tuple,
    Type,
    TypeVar,
    overload,
)

from .enums import UserFlags

_F = TypeVar('_F', bound=flag_value)
_I = TypeVar('_I', bound=Intents)
_MCF = TypeVar('_MCF', bound=MemberCacheFlags)

class flag_value:
    flag: int
    def __init__(self, func: Callable[[Any], int]) -> None: ...
    @overload
    def __get__(self: _F, instance: None, owner: Any) -> _F: ...
    @overload
    def __get__(self, instance: Any, owner: Any) -> bool: ...
    def __set__(self, instance: Any, value: bool) -> None: ...

class alias_flag_value(flag_value): ...

class BaseFlags:
    value: int = ...
    def __init__(self, **kwargs: bool) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __iter__(self) -> Iterator[Tuple[str, bool]]: ...

class SystemChannelFlags(BaseFlags):
    VALID_FLAGS: ClassVar[Dict[str, int]]

    join_notifications: flag_value
    premium_subscriptions: flag_value

class MessageFlags(BaseFlags):
    VALID_FLAGS: ClassVar[Dict[str, int]]

    crossposted: flag_value
    is_crossposted: flag_value
    suppress_embeds: flag_value
    source_message_deleted: flag_value
    urgent: flag_value

class PublicUserFlags(BaseFlags):
    VALID_FLAGS: ClassVar[Dict[str, int]]

    staff: flag_value
    partner: flag_value
    hypesquad: flag_value
    bug_hunter: flag_value
    hypesquad_bravery: flag_value
    hypesquad_brilliance: flag_value
    hypesquad_balance: flag_value
    early_supporter: flag_value
    team_user: flag_value
    system: flag_value
    bug_hunter_level_2: flag_value
    verified_bot: flag_value
    verified_bot_developer: flag_value
    early_verified_bot_developer: alias_flag_value
    def all(self) -> List[UserFlags]: ...

class Intents(BaseFlags):
    VALID_FLAGS: ClassVar[Dict[str, int]]
    def __init__(
        self,
        *,
        guilds: bool = ...,
        members: bool = ...,
        bans: bool = ...,
        emojis: bool = ...,
        integrations: bool = ...,
        webhooks: bool = ...,
        invites: bool = ...,
        voice_states: bool = ...,
        presences: bool = ...,
        messages: bool = ...,
        guild_messages: bool = ...,
        dm_messages: bool = ...,
        reactions: bool = ...,
        guild_reactions: bool = ...,
        dm_reactions: bool = ...,
        typing: bool = ...,
        guild_typing: bool = ...,
        dm_typing: bool = ...,
    ) -> None: ...
    @classmethod
    def all(cls: Type[_I]) -> _I: ...
    @classmethod
    def none(cls: Type[_I]) -> _I: ...
    @classmethod
    def default(cls: Type[_I]) -> _I: ...
    guilds: flag_value
    members: flag_value
    bans: flag_value
    emojis: flag_value
    integrations: flag_value
    webhooks: flag_value
    invites: flag_value
    voice_states: flag_value
    presences: flag_value
    messages: alias_flag_value
    guild_messages: flag_value
    dm_messages: flag_value
    reactions: alias_flag_value
    guild_reactions: flag_value
    dm_reactions: flag_value
    typing: alias_flag_value
    guild_typing: flag_value
    dm_typing: flag_value

class MemberCacheFlags(BaseFlags):
    VALID_FLAGS: ClassVar[Dict[str, int]]
    def __init__(
        self, *, online: bool = ..., voice: bool = ..., joined: bool = ...
    ) -> None: ...
    @classmethod
    def all(cls: Type[_MCF]) -> _MCF: ...
    @classmethod
    def none(cls: Type[_MCF]) -> _MCF: ...
    online: flag_value
    voice: flag_value
    joined: flag_value
    @classmethod
    def from_intents(cls: Type[_MCF], intents: Intents) -> _MCF: ...
