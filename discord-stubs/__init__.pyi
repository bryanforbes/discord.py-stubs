from typing import NamedTuple
from typing_extensions import Final

from . import abc as abc  # noqa
from . import opus as opus  # noqa
from . import utils as utils  # noqa
from .activity import *  # noqa
from .appinfo import AppInfo as AppInfo  # noqa
from .asset import Asset as Asset  # noqa
from .audit_logs import AuditLogChanges as AuditLogChanges  # noqa
from .audit_logs import AuditLogDiff as AuditLogDiff  # noqa
from .audit_logs import AuditLogEntry as AuditLogEntry  # noqa
from .calls import CallMessage as CallMessage  # noqa
from .calls import GroupCall as GroupCall  # noqa
from .channel import CategoryChannel as CategoryChannel  # noqa
from .channel import DMChannel as DMChannel  # noqa
from .channel import GroupChannel as GroupChannel  # noqa
from .channel import StoreChannel as StoreChannel  # noqa
from .channel import TextChannel as TextChannel  # noqa
from .channel import VoiceChannel as VoiceChannel  # noqa
from .client import Client as Client  # noqa
from .colour import Color as Color  # noqa
from .colour import Colour as Colour  # noqa
from .embeds import Embed as Embed  # noqa
from .emoji import Emoji as Emoji  # noqa
from .enums import *  # noqa
from .errors import *  # noqa
from .file import File as File  # noqa
from .flags import MessageFlags as MessageFlags  # noqa
from .flags import SystemChannelFlags as SystemChannelFlags  # noqa
from .guild import Guild as Guild  # noqa
from .invite import Invite as Invite  # noqa
from .member import Member as Member  # noqa
from .member import VoiceState as VoiceState  # noqa
from .message import Attachment as Attachment  # noqa
from .message import Message as Message  # noqa
from .object import Object as Object  # noqa
from .partial_emoji import PartialEmoji as PartialEmoji  # noqa
from .permissions import PermissionOverwrite as PermissionOverwrite  # noqa
from .permissions import Permissions as Permissions  # noqa
from .player import AudioSource as AudioSource  # noqa
from .player import FFmpegAudio as FFmpegAudio  # noqa
from .player import FFmpegOpusAudio as FFmpegOpusAudio  # noqa
from .player import FFmpegPCMAudio as FFmpegPCMAudio  # noqa
from .player import PCMAudio as PCMAudio  # noqa
from .player import PCMVolumeTransformer as PCMVolumeTransformer  # noqa
from .raw_models import *  # noqa
from .reaction import Reaction as Reaction  # noqa
from .relationship import Relationship as Relationship  # noqa
from .role import Role as Role  # noqa
from .shard import AutoShardedClient as AutoShardedClient  # noqa
from .team import *  # noqa
from .user import ClientUser as ClientUser  # noqa
from .user import Profile as Profile  # noqa
from .user import User as User  # noqa
from .voice_client import VoiceClient as VoiceClient  # noqa
from .webhook import *  # noqa
from .widget import Widget as Widget  # noqa
from .widget import WidgetChannel as WidgetChannel  # noqa
from .widget import WidgetMember as WidgetMember  # noqa

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
