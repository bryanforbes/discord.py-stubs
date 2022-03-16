from io import BytesIO, StringIO
from typing import BinaryIO, Optional, Union

class File:
    fp: Union[str, BinaryIO, BytesIO, StringIO]
    filename: Optional[str]
    spoiler: bool
    def __init__(
        self,
        fp: Union[str, BinaryIO, BytesIO, StringIO],
        filename: Optional[str] = ...,
        *,
        spoiler: bool = ...,
    ) -> None: ...
    def reset(self, *, seek: bool = ...) -> None: ...
    def close(self) -> None: ...
