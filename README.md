# discord.py-stubs

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://github.com/bryanforbes/discord.py-stubs/blob/master/LICENSE)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

This package contains type stubs to provide more precise static types and type inference for discord.py.

## Installation

```
pip install discord.py-stubs
```

**NOTE:** Because `discord.py` uses namespace packages for its extensions, `mypy` must be configured to use namespace packages either with the `--namespace-packages` command line flag, or by setting `namespace_packages = True` in your `mypy` configuration file. See the [import discovery](https://mypy.readthedocs.io/en/stable/command_line.html#import-discovery) section of the `mypy` documentation for more details.

## Usage Notes

In most cases, installing this package will enable developers to type check their discord.py bots using mypy out of the box. However, if developers wish to subclass the classes in `discord.ext.commands` they will need to follow the `mypy` documentation outlining how to use [classes that are generic in stubs but not at runtime](https://mypy.readthedocs.io/en/stable/common_issues.html#using-classes-that-are-generic-in-stubs-but-not-at-runtime):

```python
from typing import TYPE_CHECKING
from discord.ext import commands

class MyContext(commands.Context):
    ...

if TYPE_CHECKING:
    Cog = commands.Cog[MyContext]
else:
    Cog = commands.Cog

class MyCog(Cog):
    ...
```

In order to avoid this issue, developers can use [`discord-ext-typed-commands`](https://github.com/bryanforbes/discord-ext-typed-commands/):

```python
from discord.ext import typed_commands

class MyContext(typed_commands.Context):
    ...

class MyCog(typed_commands.Cog[MyContext]):
    ...
```

## Development

Make sure you have [poetry](https://python-poetry.org/) installed.

```
poetry install
poetry run pre-commit install --hook-type pre-commit --hook-type post-checkout
```


## Version numbering scheme

The **major** and **minor** version numbers of `discord.py-stubs` will match the **major** and **minor** version numbers of the `discord.py` release the stubs represent. For instance, if you are using `discord.py` version `1.6.4`, you would use `discord.py-stubs` version `1.6.X` where `X` is the latest **patch** version of the stubs. Using semver dependency specifications, `discord.py-stubs` version `~1.6` is designed to work with `discord.py` version `~1.6`.

In addition, `discord.py-stubs` will indicate which versions of the runtime library are compatible through its dependency information (as suggested in PEP-561).
