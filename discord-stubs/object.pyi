import datetime
from typing import SupportsInt, Text, Union
from typing_extensions import SupportsIndex

from .mixins import Hashable

class Object(Hashable):
    id: int
    def __init__(self, id: Union[Text, bytes, SupportsInt, SupportsIndex]) -> None: ...
    @property
    def created_at(self) -> datetime.datetime: ...
