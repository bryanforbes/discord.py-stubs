from typing import TYPE_CHECKING, Generic, TypeVar

from discord.ext import commands
from discord.ext.commands import core
from discord.ext.commands.core import *  # noqa

CT = TypeVar('CT', bound=commands.Context)

if TYPE_CHECKING:

    class Command(core.Command[CT]):  # type: ignore[no-redef]
        ...

    class GroupMixin(core.GroupMixin[CT]):  # type: ignore[no-redef]
        ...

    class Group(core.Group[CT]):  # type: ignore[no-redef]
        ...


else:

    class Command(core.Command, Generic[CT]):
        ...

    class GroupMixin(core.GroupMixin, Generic[CT]):
        ...

    class Group(core.Group, Generic[CT]):
        ...


__all__ = core.__all__  # type: ignore[attr-defined]
