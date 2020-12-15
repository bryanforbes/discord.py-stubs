import datetime
from typing import List, Optional, Union, type_check_only
from typing_extensions import TypedDict

from .channel import GroupChannel
from .enums import VoiceRegion
from .member import VoiceState
from .message import Message
from .user import ClientUser, User

# TODO: remove this comment when a new version of black comes out
@type_check_only
class _BaseVoiceStateDict(TypedDict):
    channel_id: Optional[int]
    user_id: int
    session_id: str
    deaf: bool
    mute: bool
    self_deaf: bool
    self_mute: bool
    suppress: bool

@type_check_only
class _VoiceStateDict(_BaseVoiceStateDict, total=False):
    guild_id: int

class CallMessage:
    ended_timestamp: Optional[datetime.datetime]
    participants: Optional[List[User]]
    message: Message
    def __init__(
        self,
        message: Message,
        *,
        ended_timestamp: Optional[str] = ...,
        participants: List[User],
    ) -> None: ...
    @property
    def call_ended(self) -> bool: ...
    @property
    def channel(self) -> GroupChannel: ...
    @property
    def duration(self) -> datetime.timedelta: ...

class GroupCall:
    call: CallMessage
    unavailable: Optional[bool]
    ringing: List[User]
    region: VoiceRegion
    def __init__(
        self,
        *,
        call: CallMessage,
        unavailable: bool,
        voice_states: List[_VoiceStateDict] = ...,
        region: VoiceRegion,
        ringing: List[int] = ...,
    ) -> None: ...
    @property
    def connected(self) -> List[Union[User, ClientUser]]: ...
    @property
    def channel(self) -> GroupChannel: ...
    def voice_state_for(
        self, user: Union[User, ClientUser]
    ) -> Optional[VoiceState]: ...
