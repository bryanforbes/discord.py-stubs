from typing import List, Optional

from .asset import Asset
from .guild import _VALID_STATIC_ICON_FORMATS, Guild
from .team import Team
from .user import User

class AppInfo:
    id: int
    name: str
    description: Optional[str]
    icon: Optional[str]
    rpc_origins: Optional[List[str]]
    bot_public: bool
    bot_require_code_grant: bool
    owner: User
    team: Team
    summary: str
    verify_key: str
    guild_id: Optional[int]
    primary_sku_id: Optional[int]
    slug: Optional[str]
    cover_image: Optional[str]
    @property
    def icon_url(self) -> Asset: ...
    def icon_url_as(
        self, *, format: _VALID_STATIC_ICON_FORMATS = ..., size: int = ...
    ) -> Asset: ...
    @property
    def cover_image_url(self) -> Asset: ...
    def cover_image_url_as(
        self, *, format: _VALID_STATIC_ICON_FORMATS = ..., size: int = ...
    ) -> Asset: ...
    @property
    def guild(self) -> Optional[Guild]: ...
