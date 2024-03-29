from ctypes import Structure, c_float, c_int, c_int16, pointer
from typing import Any, ClassVar, Optional, Type, Union, type_check_only
from typing_extensions import Final, TypedDict

from .errors import DiscordException

c_int_ptr: Final[Type[pointer[c_int]]]
c_int16_ptr: Final[Type[pointer[c_int16]]]
c_float_ptr: Final[Type[pointer[c_float]]]

class EncoderStruct(Structure): ...
class DecoderStruct(Structure): ...

EncoderStructPtr: Final[Type[pointer[EncoderStruct]]]
DecoderStructPtr: Final[Type[pointer[DecoderStruct]]]

OK: Final[int]
BAD_ARG: Final[int]
APPLICATION_AUDIO: Final[int]
APPLICATION_VOIP: Final[int]
APPLICATION_LOWDELAY: Final[int]
CTL_SET_BITRATE: Final[int]
CTL_SET_BANDWIDTH: Final[int]
CTL_SET_FEC: Final[int]
CTL_SET_PLP: Final[int]
CTL_SET_SIGNAL: Final[int]
CTL_SET_GAIN: Final[int]
CTL_LAST_PACKET_DURATION: Final[int]

@type_check_only
class _BandCtl(TypedDict):
    narrow: int
    medium: int
    wide: int
    superwide: int
    full: int

@type_check_only
class _SignalCtl(TypedDict):
    auto: int
    voice: int
    music: int

band_ctl: Final[_BandCtl]
signal_ctl: Final[_SignalCtl]

def libopus_loader(name: str) -> Any: ...
def load_opus(name: str) -> None: ...
def is_loaded() -> bool: ...

class OpusError(DiscordException):
    code: int

class OpusNotLoaded(DiscordException): ...

class _OpusStruct:
    SAMPLING_RATE: ClassVar[int]
    CHANNELS: ClassVar[int]
    FRAME_LENGTH: ClassVar[int]
    SAMPLE_SIZE: ClassVar[int]
    SAMPLES_PER_FRAME: ClassVar[int]
    FRAME_SIZE: ClassVar[int]
    @staticmethod
    def get_opus_version() -> str: ...

class Encoder(_OpusStruct):
    application: int
    def __init__(self, application: int = ...) -> None: ...
    def __del__(self) -> None: ...
    def set_bitrate(self, kbps: int) -> int: ...
    def set_bandwidth(self, req: str) -> None: ...
    def set_signal_type(self, req: str) -> None: ...
    def set_fec(self, enabled: bool = ...) -> None: ...
    def set_expected_packet_loss_percent(
        self, percentage: Union[int, float]
    ) -> None: ...
    def encode(self, pcm: bytes, frame_size: int) -> bytes: ...

class Decoder(_OpusStruct):
    def __init__(self) -> None: ...
    def __del__(self) -> None: ...
    @staticmethod
    def packet_get_nb_frames(data: bytes) -> int: ...
    @staticmethod
    def packet_get_nb_channels(data: bytes) -> int: ...
    @classmethod
    def packet_get_samples_per_frame(cls, data: bytes) -> int: ...
    def set_gain(self, dB: int) -> int: ...
    def set_volume(self, mult: int) -> int: ...
    def decode(self, data: Optional[bytes], *, fec: bool = ...) -> bytes: ...
