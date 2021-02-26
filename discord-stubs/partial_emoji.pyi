from datetime import datetime
from typing import Any, Optional, Type, TypeVar

from .asset import _VALID_ANIMATED_ICON_FORMATS, _VALID_STATIC_ICON_FORMATS, Asset
from .http import _PartialEmojiDict

class _EmojiTag: ...

_PE = TypeVar('_PE', bound=PartialEmoji)

class PartialEmoji(_EmojiTag):
    animated: bool
    name: Optional[str]
    id: Optional[int]
    @classmethod
    def from_dict(cls: Type[_PE], data: _PartialEmojiDict) -> _PE: ...
    def to_dict(self) -> _PartialEmojiDict: ...
    @classmethod
    def with_state(
        cls: Type[_PE],
        state: Any,
        *,
        name: Optional[str],
        animated: bool = ...,
        id: Optional[int] = ...,
    ) -> _PE: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def is_custom_emoji(self) -> bool: ...
    def is_unicode_emoji(self) -> bool: ...
    @property
    def created_at(self) -> Optional[datetime]: ...
    @property
    def url(self) -> Asset: ...
    def url_as(
        self,
        *,
        format: Optional[_VALID_ANIMATED_ICON_FORMATS] = ...,
        static_format: _VALID_STATIC_ICON_FORMATS = ...,
    ) -> Asset: ...
