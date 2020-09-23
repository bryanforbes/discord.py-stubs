from typing import NamedTuple
from typing_extensions import Final

from . import abc as abc  # noqa: F401
from . import opus as opus  # noqa: F401
from . import utils as utils  # noqa: F401
from .activity import *  # noqa: F401
from .appinfo import AppInfo as AppInfo  # noqa: F401
from .asset import Asset as Asset  # noqa: F401
from .audit_logs import AuditLogChanges as AuditLogChanges  # noqa: F401
from .audit_logs import AuditLogDiff as AuditLogDiff  # noqa: F401
from .audit_logs import AuditLogEntry as AuditLogEntry  # noqa: F401
from .calls import CallMessage as CallMessage  # noqa: F401
from .calls import GroupCall as GroupCall  # noqa: F401
from .channel import CategoryChannel as CategoryChannel  # noqa: F401
from .channel import DMChannel as DMChannel  # noqa: F401
from .channel import GroupChannel as GroupChannel  # noqa: F401
from .channel import StoreChannel as StoreChannel  # noqa: F401
from .channel import TextChannel as TextChannel  # noqa: F401
from .channel import VoiceChannel as VoiceChannel  # noqa: F401
from .client import Client as Client  # noqa: F401
from .colour import Color as Color  # noqa: F401
from .colour import Colour as Colour  # noqa: F401
from .embeds import Embed as Embed  # noqa: F401
from .emoji import Emoji as Emoji  # noqa: F401
from .enums import *  # noqa: F401
from .errors import *  # noqa: F401
from .file import File as File  # noqa: F401
from .flags import Intents as Intents  # noqa: F401
from .flags import MemberCacheFlags as MemberCacheFlags  # noqa: F401
from .flags import MessageFlags as MessageFlags  # noqa: F401
from .flags import PublicUserFlags as PublicUserFlags  # noqa: F401
from .flags import SystemChannelFlags as SystemChannelFlags  # noqa: F401
from .guild import Guild as Guild  # noqa: F401
from .integrations import Integration as Integration  # noqa: F401
from .integrations import IntegrationAccount as IntegrationAccount  # noqa: F401
from .invite import Invite as Invite  # noqa: F401
from .member import Member as Member  # noqa: F401
from .member import VoiceState as VoiceState  # noqa: F401
from .mentions import AllowedMentions as AllowedMentions  # noqa: F401
from .message import Attachment as Attachment  # noqa: F401
from .message import Message as Message  # noqa: F401
from .message import MessageReference as MessageReference  # noqa: F401
from .object import Object as Object  # noqa: F401
from .partial_emoji import PartialEmoji as PartialEmoji  # noqa: F401
from .permissions import PermissionOverwrite as PermissionOverwrite  # noqa: F401
from .permissions import Permissions as Permissions  # noqa: F401
from .player import AudioSource as AudioSource  # noqa: F401
from .player import FFmpegAudio as FFmpegAudio  # noqa: F401
from .player import FFmpegOpusAudio as FFmpegOpusAudio  # noqa: F401
from .player import FFmpegPCMAudio as FFmpegPCMAudio  # noqa: F401
from .player import PCMAudio as PCMAudio  # noqa: F401
from .player import PCMVolumeTransformer as PCMVolumeTransformer  # noqa: F401
from .raw_models import *  # noqa: F401
from .reaction import Reaction as Reaction  # noqa: F401
from .relationship import Relationship as Relationship  # noqa: F401
from .role import Role as Role  # noqa: F401
from .shard import AutoShardedClient as AutoShardedClient  # noqa: F401
from .shard import ShardInfo as ShardInfo  # noqa: F401
from .team import *  # noqa: F401
from .template import Template as Template  # noqa: F401
from .user import ClientUser as ClientUser  # noqa: F401
from .user import Profile as Profile  # noqa: F401
from .user import User as User  # noqa: F401
from .voice_client import VoiceClient as VoiceClient  # noqa: F401
from .voice_client import VoiceProtocol as VoiceProtocol  # noqa: F401
from .webhook import *  # noqa: F401
from .widget import Widget as Widget  # noqa: F401
from .widget import WidgetChannel as WidgetChannel  # noqa: F401
from .widget import WidgetMember as WidgetMember  # noqa: F401

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int

__title__: Final[str] = ...
__author__: Final[str] = ...
__license__: Final[str] = ...
__copyright__: Final[str] = ...
__version__: Final[str] = ...
version_info: Final[VersionInfo] = ...
