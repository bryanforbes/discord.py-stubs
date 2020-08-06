from typing import TYPE_CHECKING, Generic, TypeVar

from discord.ext import commands
from discord.ext.commands import cog
from discord.ext.commands.cog import *  # noqa

CT = TypeVar('CT', bound=commands.Context)

if TYPE_CHECKING:

    class Cog(cog.Cog[CT]):  # type: ignore[no-redef]
        ...


else:

    class Command(cog.Cog, Generic[CT]):
        ...


__all__ = cog.__all__  # type: ignore[attr-defined]
