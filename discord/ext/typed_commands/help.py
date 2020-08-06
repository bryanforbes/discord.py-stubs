from typing import TYPE_CHECKING, Generic, TypeVar

from discord.ext import commands
from discord.ext.commands import help
from discord.ext.commands.help import *  # noqa

CT = TypeVar('CT', bound=commands.Context)

if TYPE_CHECKING:

    class HelpCommand(help.HelpCommand[CT]):  # type: ignore[no-redef]
        ...

    class DefaultHelpCommand(help.DefaultHelpCommand[CT]):  # type: ignore[no-redef]
        ...

    class MinimalHelpCommand(help.MinimalHelpCommand[CT]):  # type: ignore[no-redef]
        ...


else:

    class HelpCommand(help.HelpCommand, Generic[CT]):
        ...

    class DefaultHelpCommand(help.DefaultHelpCommand, Generic[CT]):
        ...

    class MinimalHelpCommand(help.MinimalHelpCommand, Generic[CT]):
        ...


__all__ = help.__all__  # type: ignore[attr-defined]
