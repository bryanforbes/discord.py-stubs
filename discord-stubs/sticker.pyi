from datetime import datetime
from typing import List, Optional

from .asset import Asset
from .enums import StickerType
from .mixins import Hashable

class Sticker(Hashable):
    id: int
    name: str
    description: str
    pack_id: int
    format: StickerType
    image: str
    tags: List[str]
    preview_image: Optional[str]
    @property
    def created_at(self) -> datetime: ...
    @property
    def image_url(self) -> Asset: ...
    def image_url_as(self, *, size: int = ...) -> Optional[Asset]: ...
