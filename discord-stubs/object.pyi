import datetime
from builtins import _SupportsIndex
from typing import SupportsInt, Text, Union

from .mixins import Hashable

class Object(Hashable):
    id: int
    def __init__(self, id: Union[Text, bytes, SupportsInt, _SupportsIndex]) -> None: ...
    @property
    def created_at(self) -> datetime.datetime: ...
