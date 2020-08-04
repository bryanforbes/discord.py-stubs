import sys
from typing import Type
from typing_extensions import Final

from mypy.plugin import Plugin

from .plugin import DiscordPlugin

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata


__version__: Final[str] = importlib_metadata.version('discord.py-stubs')


def plugin(version: str) -> Type[Plugin]:
    return DiscordPlugin
