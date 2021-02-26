import datetime
from typing import Any, Optional

from .enums import VoiceRegion
from .guild import Guild
from .user import User

class Template:
    code: str
    uses: int
    name: str
    description: Optional[str]
    creator: User
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]
    source_guild: Guild
    async def create_guild(
        self, name: str, region: Optional[VoiceRegion] = ..., icon: Optional[Any] = ...
    ) -> Guild: ...
    async def sync(self) -> None: ...
    async def edit(
        self, *, name: str = ..., description: Optional[str] = ...
    ) -> None: ...
    async def delete(self) -> None: ...
