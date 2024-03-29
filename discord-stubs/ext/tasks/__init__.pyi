import asyncio
import datetime
from typing import (
    Any,
    Awaitable,
    Callable,
    Generator,
    Generic,
    Optional,
    Type,
    TypeVar,
    Union,
    overload,
    type_check_only,
)
from typing_extensions import Protocol

_T = TypeVar('_T')
_L = TypeVar('_L', bound=Loop[Any])
_CoroType = Callable[..., Union[Awaitable[_T], Generator[Any, None, _T]]]
_C = TypeVar('_C', bound=Callable[..., Awaitable[Any]])

@type_check_only
class _LoopCallback(Protocol):
    async def __call__(self) -> Any: ...

@type_check_only
class _ErrorCallback(Protocol):
    async def __call__(self, __exc: BaseException) -> Any: ...

class Loop(Generic[_T]):
    coro: _CoroType[_T]
    seconds: float
    hours: float
    minutes: float
    reconnect: bool
    loop: asyncio.AbstractEventLoop
    count: Optional[int]
    def __init__(
        self,
        coro: _CoroType[_T],
        seconds: float,
        hours: float,
        minutes: float,
        count: Optional[int],
        reconnect: bool,
        loop: Optional[asyncio.AbstractEventLoop],
    ) -> None: ...
    @overload
    def __get__(self: _L, obj: None, objtype: Any) -> _L: ...
    @overload
    def __get__(self, obj: Any, objtype: Any) -> Loop[_T]: ...
    @property
    def current_loop(self) -> int: ...
    @property
    def next_iteration(self) -> Optional[datetime.datetime]: ...
    async def __call__(self, *args: Any, **kwargs: Any) -> _T: ...
    def start(self, *args: Any, **kwargs: Any) -> asyncio.Task[_T]: ...
    def stop(self) -> None: ...
    def cancel(self) -> None: ...
    def restart(self, *args: Any, **kwargs: Any) -> None: ...
    def add_exception_type(self, *exceptions: Type[BaseException]) -> None: ...
    def clear_exception_types(self) -> None: ...
    def remove_exception_type(self, *exceptions: Type[BaseException]) -> bool: ...
    def get_task(self) -> asyncio.Task[_T]: ...
    def is_being_cancelled(self) -> bool: ...
    def failed(self) -> bool: ...
    def is_running(self) -> bool: ...
    def before_loop(self, coro: _LoopCallback) -> _LoopCallback: ...
    def after_loop(self, coro: _LoopCallback) -> _LoopCallback: ...
    def error(self, coro: _ErrorCallback) -> _ErrorCallback: ...
    def change_interval(
        self, *, seconds: float = ..., minutes: float = ..., hours: float = ...
    ) -> None: ...

def loop(
    *,
    seconds: float = ...,
    minutes: float = ...,
    hours: float = ...,
    count: Optional[int] = ...,
    reconnect: bool = ...,
    loop: Optional[asyncio.AbstractEventLoop] = ...,
) -> Callable[[_CoroType[_T]], Loop[_T]]: ...
