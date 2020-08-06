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

## Development

Make sure you have [poetry](https://python-poetry.org/) installed.

```
poetry install
poetry run pre-commit install --hook-type pre-commit --hook-type post-checkout
```


## Version numbering scheme

At this time, the version number of `discord.py-stubs` will follow the version number of `discord.py` it corresponds to and append one more version segment that indicates the sequence of releases for the stubs. For instance, if you are using `discord.py` version `1.3.4`, you would use `discord.py-stubs` version `1.3.4.X` where `X` is an integer.
