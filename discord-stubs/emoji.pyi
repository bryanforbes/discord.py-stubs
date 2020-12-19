import datetime
from typing import Any, Iterator, List, Optional, Tuple

from .asset import Asset
from .guild import _VALID_ANIMATED_ICON_FORMATS, _VALID_STATIC_ICON_FORMATS, Guild
from .partial_emoji import _EmojiTag
from .role import Role
from .user import User

class Emoji(_EmojiTag):
    name: str
    id: int
    require_colons: bool
    animated: bool
    managed: bool
    guild_id: int
    available: bool
    user: Optional[User]
    def __iter__(self) -> Iterator[Tuple[str, Any]]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    @property
    def created_at(self) -> datetime.datetime: ...
    @property
    def url(self) -> Asset: ...
    @property
    def roles(self) -> List[Role]: ...
    @property
    def guild(self) -> Guild: ...
    def url_as(
        self,
        *,
        format: Optional[_VALID_ANIMATED_ICON_FORMATS] = ...,
        static_format: _VALID_STATIC_ICON_FORMATS = ...,
    ) -> Asset: ...
    def is_usable(self) -> bool: ...
    async def delete(self, *, reason: Optional[str] = ...) -> None: ...
    async def edit(
        self,
        *,
        name: Optional[str] = ...,
        roles: Optional[List[Role]] = ...,
        reason: Optional[str] = ...,
    ) -> None: ...
