from typing import TypeVar

from discord.ext import commands
from discord.ext.commands import *  # noqa

CT = TypeVar('CT', bound=commands.Context)

class Bot(commands.Bot[CT]): ...  # type: ignore[no-redef]
class AutoShardedBot(commands.AutoShardedBot[CT]): ...  # type: ignore[no-redef]
class Cog(commands.Cog[CT]): ...  # type: ignore[no-redef]
class Command(commands.Command[CT]): ...  # type: ignore[no-redef]
class GroupMixin(commands.GroupMixin[CT]): ...  # type: ignore[no-redef]
class Group(commands.Group[CT]): ...  # type: ignore[no-redef]
class HelpCommand(commands.HelpCommand[CT]): ...  # type: ignore[no-redef]
class DefaultHelpCommand(commands.DefaultHelpCommand[CT]): ...  # type: ignore[no-redef]
class MinimalHelpCommand(commands.MinimalHelpCommand[CT]): ...  # type: ignore[no-redef]
