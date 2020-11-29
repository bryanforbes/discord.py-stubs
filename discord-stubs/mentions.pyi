from typing import Any, Iterable, List, Type, TypeVar, Union
from typing_extensions import TypedDict

from .abc import Snowflake

_AM = TypeVar('_AM', bound=AllowedMentions)

class _FakeBool:
    def __eq__(self, other: Any) -> bool: ...
    def __bool__(self) -> bool: ...

default: _FakeBool

class _AllowedMentionsDictBase(TypedDict):
    parse: List[str]

class _AllowedMentionsDict(_AllowedMentionsDictBase, total=False):
    users: List[int]
    roles: List[int]
    replied_user: bool

class AllowedMentions:
    everyone: bool
    users: Union[bool, Iterable[Snowflake]]
    roles: Union[bool, Iterable[Snowflake]]
    replied_user: bool
    def __init__(
        self,
        *,
        everyone: Union[bool, _FakeBool] = ...,
        users: Union[bool, _FakeBool, Iterable[Snowflake]] = ...,
        roles: Union[bool, _FakeBool, Iterable[Snowflake]] = ...,
        replied_user: Union[bool, _FakeBool] = ...,
    ) -> None: ...
    @classmethod
    def all(cls: Type[_AM]) -> _AM: ...
    @classmethod
    def none(cls: Type[_AM]) -> _AM: ...
    def to_dict(self) -> _AllowedMentionsDict: ...
    def merge(self, other: AllowedMentions) -> AllowedMentions: ...
