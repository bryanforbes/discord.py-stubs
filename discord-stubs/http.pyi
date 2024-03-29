import asyncio
from typing import (
    Any,
    BinaryIO,
    ClassVar,
    Coroutine,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Union,
    type_check_only,
)
from typing_extensions import TypedDict

import aiohttp

from .file import File
from .mentions import _AllowedMentionsDict
from .message import _MessageReferenceDict

@type_check_only
class _ApplicationDict(TypedDict):
    id: int
    cover_image: str
    description: str
    icon: str
    name: str

@type_check_only
class _BaseUserDict(TypedDict):
    id: int
    username: str
    discriminator: str
    avatar: Optional[str]

@type_check_only
class _UserDict(_BaseUserDict, total=False):
    bot: bool
    mfa_enabled: bool
    verified: bool
    email: str
    premium: bool

@type_check_only
class _BaseApplicationInfoDict(TypedDict):
    id: int
    name: str
    bot_public: bool
    bot_require_code_grant: bool
    owner: _UserDict

@type_check_only
class _ApplicationInfoDict(_BaseApplicationInfoDict, total=False):
    icon: str
    description: str
    rpc_origins: List[str]

@type_check_only
class _AttachmentDict(TypedDict):
    id: int
    filename: str
    size: int
    url: str
    proxy_url: str
    height: Optional[int]
    width: Optional[int]

@type_check_only
class _EmbedFooterDict(TypedDict, total=False):
    text: str
    icon_url: str
    proxy_icon_url: str

@type_check_only
class _BaseEmbedMediaDict(TypedDict):
    url: str

@type_check_only
class _EmbedMediaDict(_BaseEmbedMediaDict, total=False):
    height: int
    width: int

@type_check_only
class _EmbedImageDict(_EmbedMediaDict, total=False):
    proxy_url: str

@type_check_only
class _EmbedProviderDict(TypedDict):
    name: str
    url: str

@type_check_only
class _EmbedAuthorDict(TypedDict, total=False):
    name: str
    url: str
    icon_url: str
    proxy_icon_url: str

@type_check_only
class _BaseEmbedFieldDict(TypedDict):
    name: str
    value: str

@type_check_only
class _EmbedFieldDict(_BaseEmbedFieldDict, total=False):
    inline: bool

@type_check_only
class _EmbedDict(TypedDict, total=False):
    type: str
    title: str
    description: str
    url: str
    timestamp: str
    color: int
    footer: _EmbedFooterDict
    image: _EmbedImageDict
    thumbnail: _EmbedImageDict
    video: _EmbedMediaDict
    provider: _EmbedProviderDict
    author: _EmbedAuthorDict
    fields: List[_EmbedFieldDict]

@type_check_only
class _PositionDict(TypedDict):
    id: int
    position: int

@type_check_only
class _OverwriteDict(TypedDict):
    id: int
    type: str
    allow: int
    deny: int

@type_check_only
class _BaseChannelDict(TypedDict):
    id: int
    type: int

@type_check_only
class _ChannelDict(_BaseChannelDict, total=False):
    guild_id: int
    position: int
    permission_overwrites: List[_OverwriteDict]
    name: str
    topic: str
    nsfw: bool
    last_message_id: Optional[int]
    bitrate: int
    user_limit: int
    recipients: List[_UserDict]
    icon: Optional[str]
    owner_id: int
    application_id: int
    parent_id: Optional[int]
    last_pin_timestamp: str

@type_check_only
class _ClientUserDict(TypedDict):
    afk_timeout: int
    animate_emojis: bool
    convert_emoticons: bool
    default_guilds_restricted: bool
    detect_platform_accounts: bool
    developer_mode: bool
    disable_games_tab: bool
    enable_tts_command: bool
    explicit_content_filter: int
    friend_source_flags: int
    gif_auto_play: bool
    guild_positions: List[int]
    inline_attachment_media: bool
    inline_embed_media: bool
    locale: str
    message_display_compact: bool
    render_embeds: bool
    render_reactions: bool
    restricted_guilds: List[int]
    show_current_game: bool
    status: str
    theme: str
    timezone_offset: int

@type_check_only
class _BaseMessageDict(TypedDict):
    id: int
    channel_id: int
    author: _UserDict
    content: str
    timestamp: str
    edited_timestamp: Optional[str]
    tts: bool
    mention_everyone: bool
    mentions: List[_UserDict]
    mention_roles: List[int]
    attachments: List[_AttachmentDict]
    embeds: List[_EmbedDict]
    pinned: bool
    type: int

@type_check_only
class _BaseMessageActivityDict(TypedDict):
    type: int

@type_check_only
class _MessageActivityDict(_BaseMessageActivityDict, total=False):
    party_id: str

@type_check_only
class _MessageCallDict(TypedDict, total=False):
    participants: List[int]

@type_check_only
class _BasePartialEmojiDict(TypedDict):
    id: Optional[int]
    name: str

@type_check_only
class _PartialEmojiDict(_BasePartialEmojiDict, total=False):
    animated: bool

@type_check_only
class _ReactionDict(TypedDict):
    count: int
    me: bool
    emoji: _PartialEmojiDict

@type_check_only
class _BaseEmojiDict(TypedDict):
    id: int
    name: str

@type_check_only
class _EmojiDict(_BaseEmojiDict, total=False):
    animated: bool
    roles: List[int]
    user: _UserDict
    require_colons: bool
    managed: bool

@type_check_only
class _MessageDict(_BaseMessageDict, total=False):
    reactions: List[_ReactionDict]
    nonce: int
    webhook_id: int
    activity: _MessageActivityDict
    application: Any
    call: _MessageCallDict
    guild_id: int

@type_check_only
class _BaseGuildMemberDict(TypedDict):
    user: _UserDict
    roles: List[int]
    joined_at: str
    deaf: bool
    mute: bool

@type_check_only
class _GuildMemberDict(_BaseGuildMemberDict, total=False):
    nick: str
    guild_id: str

@type_check_only
class _RoleDict(TypedDict):
    id: int
    name: str
    color: int
    hoist: bool
    position: int
    permissions: int
    managed: bool
    mentionable: bool

@type_check_only
class _BaseInviteDict(TypedDict):
    code: str
    guild: Any
    channel: Any

@type_check_only
class _InviteDict(_BaseInviteDict, total=False):
    approximate_presence_count: int
    approximate_member_count: int

@type_check_only
class _InviteMetaDict(_InviteDict):
    inviter: _UserDict
    uses: int
    max_uses: int
    max_age: int
    temporary: bool
    created_at: str
    revoked: bool

@type_check_only
class _BaseWebhookDict(TypedDict):
    id: int
    token: str

@type_check_only
class _WebhookDict(_BaseWebhookDict, total=False):
    channel_id: int
    name: Optional[str]
    avatar: Optional[str]
    guild_id: int
    user: _UserDict

@type_check_only
class _GuildBanDict(TypedDict):
    reason: Optional[str]
    user: _UserDict

@type_check_only
class _GuildPruneDict(TypedDict):
    pruned: int

@type_check_only
class _TimestampsDict(TypedDict, total=False):
    start: int
    end: int

@type_check_only
class _ActivityPartyDict(TypedDict, total=False):
    id: str
    size: List[int]

@type_check_only
class _ActivityAssetsDict(TypedDict, total=False):
    large_image: str
    large_text: str
    small_image: str
    small_text: str

@type_check_only
class _BaseActivityDict(TypedDict):
    name: str
    type: int

@type_check_only
class _ActivityDict(_BaseActivityDict, total=False):
    url: Optional[str]
    timestamps: _TimestampsDict
    application_id: int
    details: Optional[str]
    state: Optional[str]
    party: _ActivityPartyDict
    assets: _ActivityAssetsDict

@type_check_only
class _SpotifyActivityDict(TypedDict, total=False):
    name: str
    url: Optional[str]
    timestamps: _TimestampsDict
    application_id: int
    details: Optional[str]
    state: Optional[str]
    party: _ActivityPartyDict
    assets: _ActivityAssetsDict
    flags: int
    sync_id: str
    session_id: str

@type_check_only
class _BaseCustomActivityDict(TypedDict):
    type: int
    name: Optional[str]

@type_check_only
class _CustomActivityDict(_BaseCustomActivityDict, total=False):
    state: str
    emoji: _EmojiDict

@type_check_only
class _PresenceUpdateDict(TypedDict):
    user: _UserDict
    roles: List[int]
    game: Optional[_ActivityDict]
    guild_id: int
    status: str

@type_check_only
class _BaseGuildDict(TypedDict):
    id: int
    name: str
    icon: Optional[str]
    splash: Optional[str]
    owner_id: int
    region: str
    afk_channel_id: Optional[int]
    afk_timeout: int
    verification_level: int
    default_message_notifications: int
    explicit_content_filter: int
    roles: List[_RoleDict]
    emojis: List[_EmojiDict]
    features: List[str]
    mfa_level: int
    application_id: Optional[int]
    system_channel_id: Optional[int]

@type_check_only
class _GuildDict(_BaseGuildDict, total=False):
    owner: bool
    permissions: int
    embed_enabled: bool
    embed_channel_id: int
    widget_enabled: bool
    widget_channel_id: int
    joined_at: str
    large: bool
    unavailable: bool
    member_count: int
    voice_states: List[Any]
    members: List[_GuildMemberDict]
    channels: List[_ChannelDict]
    presences: List[_PresenceUpdateDict]

@type_check_only
class _BaseAuditLogChangeDict(TypedDict):
    key: str

@type_check_only
class _AuditLogChangeDict(_BaseAuditLogChangeDict, total=False):
    new_value: Any
    old_value: Any

@type_check_only
class _BaseAuditLogEntryDict(TypedDict):
    target_id: Optional[str]
    user_id: int
    id: int
    action_type: int

@type_check_only
class _AuditLogEntryDict(_BaseAuditLogEntryDict, total=False):
    changes: List[_AuditLogChangeDict]
    options: Any
    reason: str

@type_check_only
class _AuditLogDict(TypedDict):
    webhooks: List[_WebhookDict]
    users: List[_UserDict]
    audit_log_entries: List[_AuditLogEntryDict]

@type_check_only
class _CurrentUserGuildDict(TypedDict):
    id: int
    name: str
    icon: str
    owner: bool
    permissions: int

@type_check_only
class _BaseVoiceStateDict(TypedDict):
    request_to_speak_timestamp: Optional[str]
    channel_id: int

@type_check_only
class _VoiceStateDict(_BaseVoiceStateDict, total=False):
    suppress: bool

@type_check_only
class _WidgetChannelDict(TypedDict):
    id: int
    name: str
    position: int

@type_check_only
class _BaseWidgetMemberDict(TypedDict):
    id: int
    username: str
    discriminator: str
    nick: str
    status: str

@type_check_only
class _WidgetMemberDict(_BaseWidgetMemberDict, total=False):
    channel_id: int
    avatar: str
    bot: bool
    deaf: bool
    self_deaf: bool
    mute: bool
    self_mute: bool
    suppress: bool
    activity: Union[_ActivityDict, _SpotifyActivityDict]

@type_check_only
class _BaseWidgetDict(TypedDict):
    id: int
    name: str

@type_check_only
class _WidgetDict(_BaseWidgetDict, total=False):
    instant_invite: Optional[str]
    channels: List[_WidgetChannelDict]
    members: List[_WidgetMemberDict]

@type_check_only
class _BaseTemplateDict(TypedDict):
    code: str
    usage_count: int
    name: str
    description: Optional[str]
    source_guild_id: int
    serialized_source_guild: _GuildDict

@type_check_only
class _TemplateDict(_BaseTemplateDict, total=False):
    creator: _UserDict
    created_at: str
    updated_at: str

@type_check_only
class _BaseCreateTemplateDict(TypedDict):
    name: str

@type_check_only
class _CreateTemplateDict(TypedDict, total=False):
    description: Optional[str]

@type_check_only
class _IntegrationAccountDict(TypedDict):
    id: int
    name: str

@type_check_only
class _BaseIntegrationDict(TypedDict):
    id: int
    name: str
    type: str
    enabled: bool
    syncing: bool
    role_id: bool
    expire_behavior: int
    expire_grace_period: int
    user: _UserDict
    account: _IntegrationAccountDict
    synced_at: str

@type_check_only
class _IntegrationDict(_BaseIntegrationDict, total=False):
    enable_emoticons: bool

async def json_or_text(response: Any) -> Any: ...

class Route:
    BASE: ClassVar[str]
    channel_id: Optional[int]
    guild_id: Optional[int]
    def __init__(self, method: str, path: str, **parameters: Any) -> None: ...
    @property
    def bucket(self) -> str: ...

class MaybeUnlock:
    def __init__(self, lock: asyncio.Lock) -> None: ...
    def __enter__(self) -> MaybeUnlock: ...
    def defer(self) -> None: ...
    def __exit__(self, type: Any, value: Any, traceback: Any) -> None: ...

class HTTPClient:
    SUCCESS_LOG: ClassVar[str]
    REQUEST_LOG: ClassVar[str]

    loop: asyncio.AbstractEventLoop
    connector: Optional[aiohttp.BaseConnector]
    token: Optional[str]
    bot_token: bool
    proxy: Optional[str]
    proxy_auth: Optional[aiohttp.BasicAuth]
    user_agent: str
    use_clock: bool
    def recreate(self) -> None: ...
    async def ws_connect(
        self, url: str, *, compress: int = ...
    ) -> aiohttp.ClientWebSocketResponse: ...
    async def request(
        self,
        route: Route,
        *,
        files: Optional[Iterable[File]] = ...,
        form: Optional[List[Dict[str, Any]]] = ...,
        **kwargs: Any,
    ) -> Any: ...
    async def get_from_cdn(self, url: str) -> bytes: ...
    async def close(self) -> None: ...
    async def static_login(self, token: str, *, bot: bool) -> Any: ...
    def logout(self) -> Coroutine[Any, Any, Any]: ...
    def start_group(
        self, user_id: int, recipients: List[Any]
    ) -> Coroutine[Any, Any, _ChannelDict]: ...
    def leave_group(self, channel_id: int) -> Coroutine[Any, Any, _ChannelDict]: ...
    def add_group_recipient(
        self, channel_id: int, user_id: int
    ) -> Coroutine[Any, Any, Any]: ...
    def remove_group_recipient(
        self, channel_id: int, user_id: int
    ) -> Coroutine[Any, Any, None]: ...
    def edit_group(
        self, channel_id: int, **options: Any
    ) -> Coroutine[Any, Any, _ChannelDict]: ...
    def convert_group(self, channel_id: int) -> Coroutine[Any, Any, Any]: ...
    def start_private_message(
        self, user_id: int
    ) -> Coroutine[Any, Any, _ChannelDict]: ...
    def send_message(
        self,
        channel_id: int,
        content: str,
        *,
        tts: bool = ...,
        embed: Optional[Dict[str, Any]] = ...,
        nonce: Optional[int] = ...,
        allowed_mentions: Optional[_AllowedMentionsDict] = ...,
        message_reference: Optional[_MessageReferenceDict] = ...,
    ) -> Coroutine[Any, Any, _MessageDict]: ...
    def send_typing(self, channel_id: int) -> Coroutine[Any, Any, None]: ...
    def send_files(
        self,
        channel_id: int,
        *,
        files: List[Tuple[BinaryIO, str]],
        content: Optional[str] = ...,
        tts: bool = ...,
        embed: Optional[Dict[str, Any]] = ...,
        nonce: Optional[int] = ...,
        allowed_mentions: Optional[_AllowedMentionsDict] = ...,
        message_reference: Optional[_MessageReferenceDict] = ...,
    ) -> Coroutine[Any, Any, _MessageDict]: ...
    async def ack_message(self, channel_id: int, message_id: int) -> None: ...
    def ack_guild(self, guild_id: int) -> Coroutine[Any, Any, Any]: ...
    def delete_message(
        self, channel_id: int, message_id: int, *, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, None]: ...
    def delete_messages(
        self, channel_id: int, message_ids: List[int], *, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, None]: ...
    def edit_message(
        self, channel_id: int, message_id: int, **fields: Any
    ) -> Coroutine[Any, Any, _MessageDict]: ...
    def add_reaction(
        self, channel_id: int, message_id: int, emoji: str
    ) -> Coroutine[Any, Any, None]: ...
    def remove_reaction(
        self, channel_id: int, message_id: int, emoji: str, member_id: int
    ) -> Coroutine[Any, Any, None]: ...
    def remove_own_reaction(
        self, channel_id: int, message_id: int, emoji: str
    ) -> Coroutine[Any, Any, None]: ...
    def get_reaction_users(
        self,
        channel_id: int,
        message_id: int,
        emoji: str,
        limit: int,
        after: Optional[int] = ...,
    ) -> Coroutine[Any, Any, _UserDict]: ...
    def clear_reactions(
        self, channel_id: int, message_id: int
    ) -> Coroutine[Any, Any, None]: ...
    def clear_single_reaction(
        self, channel_id: int, message_id: int, emoji: str
    ) -> Coroutine[Any, Any, None]: ...
    def get_message(
        self, channel_id: int, message_id: int
    ) -> Coroutine[Any, Any, _MessageDict]: ...
    def get_channel(self, channel_id: int) -> Coroutine[Any, Any, _ChannelDict]: ...
    def logs_from(
        self,
        channel_id: int,
        limit: int,
        before: Optional[int] = ...,
        after: Optional[int] = ...,
        around: Optional[int] = ...,
    ) -> Coroutine[Any, Any, List[_MessageDict]]: ...
    def publish_message(
        self, channel_id: int, message_id: int
    ) -> Coroutine[Any, Any, None]: ...
    def pin_message(
        self, channel_id: int, message_id: int, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, None]: ...
    def unpin_message(
        self, channel_id: int, message_id: int, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, None]: ...
    def pins_from(self, channel_id: int) -> Coroutine[Any, Any, List[_MessageDict]]: ...
    def kick(
        self, user_id: int, guild_id: int, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, None]: ...
    def ban(
        self,
        user_id: int,
        guild_id: int,
        delete_message_days: int = ...,
        reason: Optional[str] = ...,
    ) -> Coroutine[Any, Any, None]: ...
    def unban(
        self, user_id: int, guild_id: int, *, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, None]: ...
    def guild_voice_state(
        self,
        user_id: int,
        guild_id: int,
        *,
        mute: Optional[bool] = ...,
        deafen: Optional[bool] = ...,
        reason: Optional[str] = ...,
    ) -> Coroutine[Any, Any, None]: ...
    def edit_profile(
        self, password: str, username: str, avatar: str, **fields: Any
    ) -> Coroutine[Any, Any, _UserDict]: ...
    def change_my_nickname(
        self, guild_id: int, nickname: str, *, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, str]: ...
    def change_nickname(
        self, guild_id: int, user_id: int, nickname: str, *, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, None]: ...
    def edit_member(
        self, guild_id: int, user_id: int, *, reason: Optional[str] = ..., **fields: Any
    ) -> Coroutine[Any, Any, None]: ...
    def edit_my_voice_state(
        self, guild_id: int, payload: _VoiceStateDict
    ) -> Coroutine[Any, Any, None]: ...
    def edit_voice_state(
        self, guild_id: int, user_id: int, payload: _VoiceStateDict
    ) -> Coroutine[Any, Any, None]: ...
    def edit_channel(
        self, channel_id: int, *, reason: Optional[str] = ..., **options: Any
    ) -> Coroutine[Any, Any, _ChannelDict]: ...
    def bulk_channel_update(
        self, guild_id: int, data: List[_PositionDict], *, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, None]: ...
    def create_channel(
        self,
        guild_id: int,
        channel_type: int,
        *,
        reason: Optional[str] = ...,
        name: str,
        parent_id: Optional[int] = ...,
        topic: Optional[str] = ...,
        bitrate: Optional[int] = ...,
        nsfw: Optional[bool] = ...,
        user_limit: Optional[int] = ...,
        position: Optional[int] = ...,
        permission_overwrites: Optional[List[_OverwriteDict]] = ...,
        rate_limit_per_user: Optional[int] = ...,
        rtc_region: Optional[int] = ...,
    ) -> Coroutine[Any, Any, _ChannelDict]: ...
    def delete_channel(
        self, channel_id: int, *, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, _ChannelDict]: ...
    def create_webhook(
        self,
        channel_id: int,
        *,
        name: str,
        avatar: Optional[str] = ...,
        reason: Optional[str] = ...,
    ) -> Coroutine[Any, Any, _WebhookDict]: ...
    def channel_webhooks(
        self, channel_id: int
    ) -> Coroutine[Any, Any, List[_WebhookDict]]: ...
    def guild_webhooks(
        self, guild_id: int
    ) -> Coroutine[Any, Any, List[_WebhookDict]]: ...
    def get_webhook(self, webhook_id: int) -> Coroutine[Any, Any, _WebhookDict]: ...
    def follow_webhook(
        self, channel_id: int, webhook_channel_id: int, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, _WebhookDict]: ...
    def get_guilds(
        self, limit: int, before: Optional[int] = ..., after: Optional[int] = ...
    ) -> Coroutine[Any, Any, List[_CurrentUserGuildDict]]: ...
    def leave_guild(self, guild_id: int) -> Coroutine[Any, Any, None]: ...
    def get_guild(self, guild_id: int) -> Coroutine[Any, Any, _GuildDict]: ...
    def delete_guild(self, guild_id: int) -> Coroutine[Any, Any, None]: ...
    def create_guild(
        self, name: str, region: str, icon: str
    ) -> Coroutine[Any, Any, _GuildDict]: ...
    def edit_guild(
        self, guild_id: int, *, reason: Optional[str] = ..., **fields: Any
    ) -> Coroutine[Any, Any, _GuildDict]: ...
    def get_template(self, code: str) -> Coroutine[Any, Any, _TemplateDict]: ...
    def guild_templates(
        self, guild_id: int
    ) -> Coroutine[Any, Any, List[_TemplateDict]]: ...
    def create_template(
        self, guild_id: int, payload: _CreateTemplateDict
    ) -> Coroutine[Any, Any, _TemplateDict]: ...
    def sync_template(
        self, guild_id: int, code: str
    ) -> Coroutine[Any, Any, _TemplateDict]: ...
    def edit_template(
        self, guild_id: int, code: str, payload: _CreateTemplateDict
    ) -> Coroutine[Any, Any, _TemplateDict]: ...
    def delete_template(
        self, guild_id: int, code: str
    ) -> Coroutine[Any, Any, _TemplateDict]: ...
    def create_from_template(
        self, code: str, name: str, region: str, icon: str
    ) -> Coroutine[Any, Any, _GuildDict]: ...
    def get_bans(self, guild_id: int) -> Coroutine[Any, Any, List[_GuildBanDict]]: ...
    def get_ban(
        self, user_id: int, guild_id: int
    ) -> Coroutine[Any, Any, _GuildBanDict]: ...
    def get_vanity_code(self, guild_id: int) -> Coroutine[Any, Any, _InviteDict]: ...
    def change_vanity_code(
        self, guild_id: int, code: str, *, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, Any]: ...
    def prune_members(
        self,
        guild_id: int,
        days: int,
        compute_prune_count: bool,
        roles: Optional[List[int]],
        *,
        reason: Optional[str] = ...,
    ) -> Coroutine[Any, Any, _GuildPruneDict]: ...
    def get_all_guild_channels(
        self, guild_id: int
    ) -> Coroutine[Any, Any, List[_ChannelDict]]: ...
    def get_members(
        self, guild_id: int, limit: int, after: Optional[int]
    ) -> Coroutine[Any, Any, List[_GuildMemberDict]]: ...
    def get_member(
        self, guild_id: int, member_id: int
    ) -> Coroutine[Any, Any, _GuildMemberDict]: ...
    def estimate_pruned_members(
        self, guild_id: int, days: int, roles: List[str]
    ) -> Coroutine[Any, Any, _GuildPruneDict]: ...
    def get_all_custom_emojis(
        self, guild_id: int
    ) -> Coroutine[Any, Any, _EmojiDict]: ...
    def get_custom_emoji(
        self, guild_id: int, emoji_id: int
    ) -> Coroutine[Any, Any, _EmojiDict]: ...
    def create_custom_emoji(
        self,
        guild_id: int,
        name: str,
        image: str,
        *,
        roles: Optional[List[int]] = ...,
        reason: Optional[str] = ...,
    ) -> Coroutine[Any, Any, _EmojiDict]: ...
    def delete_custom_emoji(
        self, guild_id: int, emoji_id: int, *, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, None]: ...
    def edit_custom_emoji(
        self,
        guild_id: int,
        emoji_id: int,
        *,
        name: str,
        roles: Optional[List[int]] = ...,
        reason: Optional[str] = ...,
    ) -> Coroutine[Any, Any, _EmojiDict]: ...
    def get_all_integrations(
        self, guild_id: int
    ) -> Coroutine[Any, Any, List[_IntegrationDict]]: ...
    def create_integration(
        self, guild_id: int, type: str, id: int
    ) -> Coroutine[Any, Any, None]: ...
    def edit_integration(
        self, guild_id: int, integration_id: int, **payload: Any
    ) -> Coroutine[Any, Any, None]: ...
    def sync_integration(
        self, guild_id: int, integration_id: int
    ) -> Coroutine[Any, Any, None]: ...
    def delete_integration(
        self, guild_id: int, integration_id: int
    ) -> Coroutine[Any, Any, None]: ...
    def get_audit_logs(
        self,
        guild_id: int,
        limit: int = ...,
        before: Optional[int] = ...,
        after: Optional[int] = ...,
        user_id: Optional[int] = ...,
        action_type: Optional[int] = ...,
    ) -> Coroutine[Any, Any, _AuditLogDict]: ...
    def get_widget(self, guild_id: int) -> Coroutine[Any, Any, _WidgetDict]: ...
    def create_invite(
        self,
        channel_id: int,
        *,
        reason: Optional[str] = ...,
        max_age: int = ...,
        max_uses: int = ...,
        temporary: bool = ...,
        unique: bool = ...,
    ) -> Coroutine[Any, Any, _InviteDict]: ...
    def get_invite(
        self, invite_id: str, *, with_counts: bool = ...
    ) -> Coroutine[Any, Any, _InviteDict]: ...
    def invites_from(
        self, guild_id: int
    ) -> Coroutine[Any, Any, List[_InviteMetaDict]]: ...
    def invites_from_channel(
        self, channel_id: int
    ) -> Coroutine[Any, Any, List[_InviteMetaDict]]: ...
    def delete_invite(
        self, invite_id: str, *, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, _InviteDict]: ...
    def get_roles(self, guild_id: int) -> Coroutine[Any, Any, List[_RoleDict]]: ...
    def edit_role(
        self, guild_id: int, role_id: int, *, reason: Optional[str] = ..., **fields: Any
    ) -> Coroutine[Any, Any, _RoleDict]: ...
    def delete_role(
        self, guild_id: int, role_id: int, *, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, None]: ...
    def replace_roles(
        self,
        user_id: int,
        guild_id: int,
        role_ids: List[int],
        *,
        reason: Optional[str] = ...,
    ) -> Coroutine[Any, Any, _GuildMemberDict]: ...
    def create_role(
        self, guild_id: int, *, reason: Optional[str] = ..., **fields: Any
    ) -> Coroutine[Any, Any, _RoleDict]: ...
    def move_role_position(
        self,
        guild_id: int,
        positions: List[_PositionDict],
        *,
        reason: Optional[str] = ...,
    ) -> Coroutine[Any, Any, List[_RoleDict]]: ...
    def add_role(
        self, guild_id: int, user_id: int, role_id: int, *, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, None]: ...
    def remove_role(
        self, guild_id: int, user_id: int, role_id: int, *, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, None]: ...
    def edit_channel_permissions(
        self,
        channel_id: int,
        target: int,
        allow: int,
        deny: int,
        type: str,
        *,
        reason: Optional[str] = ...,
    ) -> Coroutine[Any, Any, None]: ...
    def delete_channel_permissions(
        self, channel_id: int, target: int, *, reason: Optional[str] = ...
    ) -> Coroutine[Any, Any, None]: ...
    def move_member(
        self,
        user_id: int,
        guild_id: int,
        channel_id: int,
        *,
        reason: Optional[str] = ...,
    ) -> Coroutine[Any, Any, _GuildMemberDict]: ...
    def remove_relationship(self, user_id: int) -> Coroutine[Any, Any, Any]: ...
    def add_relationship(
        self, user_id: int, type: Optional[int] = ...
    ) -> Coroutine[Any, Any, Any]: ...
    def send_friend_request(
        self, username: str, discriminator: str
    ) -> Coroutine[Any, Any, Any]: ...
    def application_info(self) -> Coroutine[Any, Any, _ApplicationInfoDict]: ...
    async def get_gateway(
        self, *, encoding: str = ..., v: int = ..., zlib: bool = ...
    ) -> str: ...
    async def get_bot_gateway(
        self, *, encoding: str = ..., v: int = ..., zlib: bool = ...
    ) -> Tuple[int, str]: ...
    def get_user(self, user_id: int) -> Coroutine[Any, Any, _UserDict]: ...
    def get_user_profile(self, user_id: int) -> Coroutine[Any, Any, Any]: ...
    def get_mutual_friends(self, user_id: int) -> Coroutine[Any, Any, _UserDict]: ...
    def change_hypesquad_house(self, house_id: int) -> Coroutine[Any, Any, Any]: ...
    def leave_hypesquad_house(self) -> Coroutine[Any, Any, None]: ...
    def edit_settings(
        self,
        *,
        afk_timeout: int = ...,
        animate_emojis: bool = ...,
        convert_emoticons: bool = ...,
        default_guilds_restricted: bool = ...,
        detect_platform_accounts: bool = ...,
        developer_mode: bool = ...,
        disable_games_tab: bool = ...,
        enable_tts_command: bool = ...,
        explicit_content_filter: int = ...,
        friend_source_flags: int = ...,
        gif_auto_play: bool = ...,
        guild_positions: List[int] = ...,
        inline_attachment_media: bool = ...,
        inline_embed_media: bool = ...,
        locale: str = ...,
        message_display_compact: bool = ...,
        render_embeds: bool = ...,
        render_reactions: bool = ...,
        restricted_guilds: List[int] = ...,
        show_current_game: bool = ...,
        status: str = ...,
        theme: str = ...,
        timezone_offset: int = ...,
    ) -> Coroutine[Any, Any, _ClientUserDict]: ...
