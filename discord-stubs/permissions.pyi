from typing import Any, ClassVar, Dict, Iterator, Optional, Set, Tuple, Type, TypeVar

from .flags import BaseFlags, flag_value

_P = TypeVar('_P', bound=Permissions)

class Permissions(BaseFlags):
    VALID_FLAGS: ClassVar[Dict[str, int]]

    create_instant_invite: flag_value
    kick_members: flag_value
    ban_members: flag_value
    administrator: flag_value
    manage_channels: flag_value
    manage_guild: flag_value
    add_reactions: flag_value
    view_audit_log: flag_value
    priority_speaker: flag_value
    stream: flag_value
    read_messages: flag_value
    view_channel: flag_value
    send_messages: flag_value
    send_tts_messages: flag_value
    manage_messages: flag_value
    embed_links: flag_value
    attach_files: flag_value
    read_message_history: flag_value
    mention_everyone: flag_value
    external_emojis: flag_value
    use_external_emojis: flag_value
    view_guild_insights: flag_value
    connect: flag_value
    speak: flag_value
    mute_members: flag_value
    deafen_members: flag_value
    move_members: flag_value
    use_voice_activation: flag_value
    change_nickname: flag_value
    manage_nicknames: flag_value
    manage_roles: flag_value
    manage_permissions: flag_value
    manage_webhooks: flag_value
    manage_emojis: flag_value
    def __init__(self, permissions: int = ..., **kwargs: bool) -> None: ...
    def is_subset(self, other: Any) -> bool: ...
    def is_superset(self, other: Any) -> bool: ...
    def is_strict_subset(self, other: Any) -> bool: ...
    def is_strict_superset(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    @classmethod
    def none(cls: Type[_P]) -> _P: ...
    @classmethod
    def all(cls: Type[_P]) -> _P: ...
    @classmethod
    def all_channel(cls: Type[_P]) -> _P: ...
    @classmethod
    def general(cls: Type[_P]) -> _P: ...
    @classmethod
    def text(cls: Type[_P]) -> _P: ...
    @classmethod
    def voice(cls: Type[_P]) -> _P: ...
    def update(
        self,
        *,
        create_instant_invite: bool = ...,
        kick_members: bool = ...,
        ban_members: bool = ...,
        administrator: bool = ...,
        manage_channels: bool = ...,
        manage_guild: bool = ...,
        add_reactions: bool = ...,
        view_audit_log: bool = ...,
        priority_speaker: bool = ...,
        stream: bool = ...,
        read_messages: bool = ...,
        view_channel: bool = ...,
        send_messages: bool = ...,
        send_tts_messages: bool = ...,
        manage_messages: bool = ...,
        embed_links: bool = ...,
        attach_files: bool = ...,
        read_message_history: bool = ...,
        mention_everyone: bool = ...,
        external_emojis: bool = ...,
        use_external_emojis: bool = ...,
        view_guild_insights: bool = ...,
        connect: bool = ...,
        speak: bool = ...,
        mute_members: bool = ...,
        deafen_members: bool = ...,
        move_members: bool = ...,
        use_voice_activation: bool = ...,
        change_nickname: bool = ...,
        manage_nicknames: bool = ...,
        manage_roles: bool = ...,
        manage_permissions: bool = ...,
        manage_webhooks: bool = ...,
        manage_emojis: bool = ...,
    ) -> None: ...
    def handle_overwrite(self, allow: int, deny: int) -> None: ...

_PO = TypeVar('_PO', bound=PermissionOverwrite)

class PermissionOverwrite:
    VALID_NAMES: ClassVar[Set[str]] = ...
    PURE_FLAGS: ClassVar[Set[str]] = ...

    create_instant_invite: Optional[bool]
    kick_members: Optional[bool]
    ban_members: Optional[bool]
    administrator: Optional[bool]
    manage_channels: Optional[bool]
    manage_guild: Optional[bool]
    add_reactions: Optional[bool]
    view_audit_log: Optional[bool]
    priority_speaker: Optional[bool]
    stream: Optional[bool]
    read_messages: Optional[bool]
    view_channel: Optional[bool]
    send_messages: Optional[bool]
    send_tts_messages: Optional[bool]
    manage_messages: Optional[bool]
    embed_links: Optional[bool]
    attach_files: Optional[bool]
    read_message_history: Optional[bool]
    mention_everyone: Optional[bool]
    external_emojis: Optional[bool]
    use_external_emojis: Optional[bool]
    view_guild_insights: Optional[bool]
    connect: Optional[bool]
    speak: Optional[bool]
    mute_members: Optional[bool]
    deafen_members: Optional[bool]
    move_members: Optional[bool]
    use_voice_activation: Optional[bool]
    change_nickname: Optional[bool]
    manage_nicknames: Optional[bool]
    manage_roles: Optional[bool]
    manage_permissions: Optional[bool]
    manage_webhooks: Optional[bool]
    manage_emojis: Optional[bool]
    def __init__(
        self,
        *,
        create_instant_invite: Optional[bool] = ...,
        kick_members: Optional[bool] = ...,
        ban_members: Optional[bool] = ...,
        administrator: Optional[bool] = ...,
        manage_channels: Optional[bool] = ...,
        manage_guild: Optional[bool] = ...,
        add_reactions: Optional[bool] = ...,
        view_audit_log: Optional[bool] = ...,
        priority_speaker: Optional[bool] = ...,
        stream: Optional[bool] = ...,
        read_messages: Optional[bool] = ...,
        view_channel: Optional[bool] = ...,
        send_messages: Optional[bool] = ...,
        send_tts_messages: Optional[bool] = ...,
        manage_messages: Optional[bool] = ...,
        embed_links: Optional[bool] = ...,
        attach_files: Optional[bool] = ...,
        read_message_history: Optional[bool] = ...,
        mention_everyone: Optional[bool] = ...,
        external_emojis: Optional[bool] = ...,
        use_external_emojis: Optional[bool] = ...,
        view_guild_insights: Optional[bool] = ...,
        connect: Optional[bool] = ...,
        speak: Optional[bool] = ...,
        mute_members: Optional[bool] = ...,
        deafen_members: Optional[bool] = ...,
        move_members: Optional[bool] = ...,
        use_voice_activation: Optional[bool] = ...,
        change_nickname: Optional[bool] = ...,
        manage_nicknames: Optional[bool] = ...,
        manage_roles: Optional[bool] = ...,
        manage_permissions: Optional[bool] = ...,
        manage_webhooks: Optional[bool] = ...,
        manage_emojis: Optional[bool] = ...,
    ) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def pair(self) -> Tuple[Permissions, Permissions]: ...
    @classmethod
    def from_pair(cls: Type[_PO], allow: Permissions, deny: Permissions) -> _PO: ...
    def is_empty(self) -> bool: ...
    def update(
        self,
        *,
        create_instant_invite: Optional[bool] = ...,
        kick_members: Optional[bool] = ...,
        ban_members: Optional[bool] = ...,
        administrator: Optional[bool] = ...,
        manage_channels: Optional[bool] = ...,
        manage_guild: Optional[bool] = ...,
        add_reactions: Optional[bool] = ...,
        view_audit_log: Optional[bool] = ...,
        priority_speaker: Optional[bool] = ...,
        stream: Optional[bool] = ...,
        read_messages: Optional[bool] = ...,
        view_channel: Optional[bool] = ...,
        send_messages: Optional[bool] = ...,
        send_tts_messages: Optional[bool] = ...,
        manage_messages: Optional[bool] = ...,
        embed_links: Optional[bool] = ...,
        attach_files: Optional[bool] = ...,
        read_message_history: Optional[bool] = ...,
        mention_everyone: Optional[bool] = ...,
        external_emojis: Optional[bool] = ...,
        use_external_emojis: Optional[bool] = ...,
        view_guild_insights: Optional[bool] = ...,
        connect: Optional[bool] = ...,
        speak: Optional[bool] = ...,
        mute_members: Optional[bool] = ...,
        deafen_members: Optional[bool] = ...,
        move_members: Optional[bool] = ...,
        use_voice_activation: Optional[bool] = ...,
        change_nickname: Optional[bool] = ...,
        manage_nicknames: Optional[bool] = ...,
        manage_roles: Optional[bool] = ...,
        manage_permissions: Optional[bool] = ...,
        manage_webhooks: Optional[bool] = ...,
        manage_emojis: Optional[bool] = ...,
    ) -> None: ...
    def __iter__(self) -> Iterator[Tuple[str, Optional[bool]]]: ...
