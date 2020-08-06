from typing import TYPE_CHECKING, Generic, TypeVar

from discord.ext import commands
from discord.ext.commands import *  # noqa

CT = TypeVar('CT', bound=commands.Context)

if TYPE_CHECKING:

    class Bot(commands.Bot[CT]):  # type: ignore[no-redef]
        ...

    class AutoShardedBot(commands.AutoShardedBot[CT]):  # type: ignore[no-redef]
        ...

    class Cog(commands.Cog[CT]):  # type: ignore[no-redef]
        ...

    class Command(commands.Command[CT]):  # type: ignore[no-redef]
        ...

    class GroupMixin(commands.GroupMixin[CT]):  # type: ignore[no-redef]
        ...

    class Group(commands.Group[CT]):  # type: ignore[no-redef]
        ...

    class HelpCommand(commands.HelpCommand[CT]):  # type: ignore[no-redef]
        ...

    class DefaultHelpCommand(commands.DefaultHelpCommand[CT]):  # type: ignore[no-redef]
        ...

    class MinimalHelpCommand(commands.MinimalHelpCommand[CT]):  # type: ignore[no-redef]
        ...


else:

    class Bot(commands.Bot, Generic[CT]):
        ...

    class AutoShardedBot(commands.AutoShardedBot, Generic[CT]):
        ...

    class Cog(commands.Cog, Generic[CT]):
        ...

    class Command(commands.Command, Generic[CT]):
        ...

    class GroupMixin(commands.GroupMixin, Generic[CT]):
        ...

    class Group(commands.Group, Generic[CT]):
        ...

    class HelpCommand(commands.HelpCommand, Generic[CT]):
        ...

    class DefaultHelpCommand(commands.DefaultHelpCommand, Generic[CT]):
        ...

    class MinimalHelpCommand(commands.MinimalHelpCommand, Generic[CT]):
        ...
