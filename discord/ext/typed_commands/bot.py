from typing import TYPE_CHECKING, Generic, TypeVar

from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.bot import *  # noqa

CT = TypeVar('CT', bound=commands.Context)

if TYPE_CHECKING:

    class BotBase(bot.BotBase[CT]):  # type: ignore[no-redef]
        ...

    class Bot(bot.Bot[CT]):  # type: ignore[no-redef]
        ...

    class AutoShardedBot(bot.AutoShardedBot[CT]):  # type: ignore[no-redef]
        ...


else:

    class BotBase(bot.BotBase, Generic[CT]):
        ...

    class Bot(bot.Bot, Generic[CT]):
        ...

    class AutoShardedBot(bot.AutoShardedBot, Generic[CT]):
        ...
