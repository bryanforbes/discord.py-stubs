from inspect import Parameter
from typing import (
    Any,
    Callable,
    Coroutine,
    Dict,
    Generic,
    Iterator,
    List,
    Mapping,
    Optional,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
    type_check_only,
)
from typing_extensions import Protocol

from ._types import _BaseCommand
from .cog import Cog
from .context import Context
from .cooldowns import Cooldown, CooldownMapping, _CooldownType

_CoroType = Callable[..., Coroutine[Any, Any, Any]]

_CT = TypeVar('_CT', bound=Context)
_C = TypeVar('_C', bound=_CoroType)
_CMD = TypeVar('_CMD', bound=Command[Any])
_F = TypeVar('_F', bound=Union[_CoroType, Command[Any]])
_T_contra = TypeVar('_T_contra', contravariant=True)

@type_check_only
class _CheckPredicate(Protocol[_T_contra]):
    def __call__(self, __ctx: _T_contra) -> Union[bool, Coroutine[Any, Any, bool]]: ...

@type_check_only
class _CheckDecorator:
    predicate: _CheckPredicate[_CT]
    def __call__(self, __func: _F) -> _F: ...

@type_check_only
class _InvokeCallback(Protocol[_T_contra]):
    async def __call__(self, __ctx: _T_contra) -> None: ...

class Command(_BaseCommand, Generic[_CT]):
    name: str
    callback: _CoroType
    help: Optional[str]
    brief: Optional[str]
    usage: Optional[str]
    aliases: Union[List[str], Tuple[str, ...]]
    enabled: bool
    parent: Optional[Command[_CT]]
    checks: List[_CheckPredicate[_CT]]
    description: str
    hidden: bool
    rest_is_raw: bool
    ignore_extra: bool
    require_var_positional: bool
    cooldown_after_parsing: bool
    params: Mapping[str, Parameter]
    _buckets: CooldownMapping
    cog: Optional[Cog[_CT]]
    def __init__(
        self,
        func: _CoroType,
        *,
        name: str = ...,
        enabled: bool = ...,
        help: Optional[str] = ...,
        brief: Optional[str] = ...,
        usage: Optional[str] = ...,
        aliases: Union[List[str], Tuple[str, ...]] = ...,
        description: str = ...,
        hidden: bool = ...,
        rest_is_raw: bool = ...,
        ignore_extra: bool = ...,
        require_var_positional: bool = ...,
        cooldown_after_parsing: bool = ...,
        checks: List[_CheckPredicate[_CT]] = ...,
        cooldown: Cooldown = ...,
        parent: _BaseCommand = ...,
        cog: Optional[Cog[_CT]] = ...,
    ) -> None: ...
    def add_check(self, func: _CheckPredicate[_CT]) -> None: ...
    def remove_check(self, func: _CheckPredicate[_CT]) -> None: ...
    def update(
        self,
        *,
        name: str = ...,
        enabled: bool = ...,
        help: Optional[str] = ...,
        brief: Optional[str] = ...,
        usage: Optional[str] = ...,
        aliases: Union[List[str], Tuple[str, ...]] = ...,
        description: str = ...,
        hidden: bool = ...,
        rest_is_raw: bool = ...,
        ignore_extra: bool = ...,
        require_var_positional: bool = ...,
        cooldown_after_parsing: bool = ...,
    ) -> None: ...
    async def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def copy(self: _CMD) -> _CMD: ...
    async def dispatch_error(self, ctx: _CT, error: Exception) -> None: ...
    async def do_conversion(
        self, ctx: _CT, converter: Any, argument: str, param: Parameter
    ) -> Any: ...
    async def transform(self, ctx: _CT, param: Parameter) -> Any: ...
    @property
    def clean_params(self) -> Mapping[str, Parameter]: ...
    @property
    def full_parent_name(self) -> str: ...
    @property
    def parents(self) -> List[Command[_CT]]: ...
    @property
    def root_parent(self) -> Optional[Command[_CT]]: ...
    @property
    def qualified_name(self) -> str: ...
    async def call_before_hooks(self, ctx: _CT) -> None: ...
    async def call_after_hooks(self, ctx: _CT) -> None: ...
    async def prepare(self, ctx: _CT) -> None: ...
    def is_on_cooldown(self, ctx: _CT) -> bool: ...
    def reset_cooldown(self, ctx: _CT) -> None: ...
    def get_cooldown_retry_after(self, ctx: _CT) -> float: ...
    async def invoke(self, ctx: _CT) -> None: ...
    async def reinvoke(self, ctx: _CT, *, call_hooks: bool = ...) -> None: ...
    def error(self, coro: _C) -> _C: ...
    def has_error_handler(self) -> bool: ...
    def before_invoke(self, coro: _C) -> _C: ...
    def after_invoke(self, coro: _C) -> _C: ...
    @property
    def cog_name(self) -> Optional[str]: ...
    @property
    def short_doc(self) -> str: ...
    @property
    def signature(self) -> str: ...
    async def can_run(self, ctx: _CT) -> bool: ...

class GroupMixin(Generic[_CT]):
    all_commands: Dict[str, Command[_CT]]
    case_insensitive: bool
    @property
    def commands(self) -> Set[Command[_CT]]: ...
    def recursively_remove_all_commands(self) -> None: ...
    def add_command(self, command: Command[_CT]) -> None: ...
    def remove_command(self, name: str) -> Optional[Command[_CT]]: ...
    def walk_commands(self) -> Iterator[Union[Command[_CT], Group[_CT]]]: ...
    def get_command(self, name: str) -> Optional[Command[_CT]]: ...
    def command(
        self,
        name: Optional[str] = ...,
        *,
        enabled: bool = ...,
        help: Optional[str] = ...,
        brief: Optional[str] = ...,
        usage: Optional[str] = ...,
        aliases: Union[List[str], Tuple[str, ...]] = ...,
        description: str = ...,
        hidden: bool = ...,
        rest_is_raw: bool = ...,
        ignore_extra: bool = ...,
        require_var_positional: bool = ...,
        cooldown_after_parsing: bool = ...,
    ) -> Callable[[_CoroType], Command[_CT]]: ...
    def group(
        self,
        name: str = ...,
        *,
        enabled: bool = ...,
        help: Optional[str] = ...,
        brief: Optional[str] = ...,
        usage: Optional[str] = ...,
        aliases: Union[List[str], Tuple[str, ...]] = ...,
        description: str = ...,
        hidden: bool = ...,
        rest_is_raw: bool = ...,
        ignore_extra: bool = ...,
        cooldown_after_parsing: bool = ...,
        invoke_without_command: bool = ...,
        case_insensitive: bool = ...,
    ) -> Callable[[_CoroType], Group[_CT]]: ...

_G = TypeVar('_G', bound=Group[Any])

class Group(GroupMixin[_CT], Command[_CT]):
    invoke_without_command: bool
    def __init__(
        self,
        *,
        name: str = ...,
        enabled: bool = ...,
        help: Optional[str] = ...,
        brief: Optional[str] = ...,
        usage: Optional[str] = ...,
        aliases: Union[List[str], Tuple[str, ...]] = ...,
        description: str = ...,
        hidden: bool = ...,
        rest_is_raw: bool = ...,
        ignore_extra: bool = ...,
        cooldown_after_parsing: bool = ...,
        invoke_without_command: bool = ...,
        case_insensitive: bool = ...,
    ) -> None: ...
    def copy(self: _G) -> _G: ...

@overload
def command(
    name: Optional[str] = ...,
    *,
    enabled: bool = ...,
    help: Optional[str] = ...,
    brief: Optional[str] = ...,
    usage: Optional[str] = ...,
    aliases: Union[List[str], Tuple[str, ...]] = ...,
    description: str = ...,
    hidden: bool = ...,
    rest_is_raw: bool = ...,
    ignore_extra: bool = ...,
    require_var_positional: bool = ...,
    cooldown_after_parsing: bool = ...,
) -> Callable[[_CoroType], Command[Any]]: ...
@overload
def command(
    name: Optional[str] = ...,
    cls: Optional[Type[Command[_CT]]] = ...,
    *,
    enabled: bool = ...,
    help: Optional[str] = ...,
    brief: Optional[str] = ...,
    usage: Optional[str] = ...,
    aliases: Union[List[str], Tuple[str, ...]] = ...,
    description: str = ...,
    hidden: bool = ...,
    rest_is_raw: bool = ...,
    ignore_extra: bool = ...,
    require_var_positional: bool = ...,
    cooldown_after_parsing: bool = ...,
) -> Callable[[_CoroType], Command[_CT]]: ...
@overload
def group(
    name: str = ...,
    *,
    enabled: bool = ...,
    help: Optional[str] = ...,
    brief: Optional[str] = ...,
    usage: Optional[str] = ...,
    aliases: Union[List[str], Tuple[str, ...]] = ...,
    description: str = ...,
    hidden: bool = ...,
    rest_is_raw: bool = ...,
    ignore_extra: bool = ...,
    cooldown_after_parsing: bool = ...,
    invoke_without_command: bool = ...,
    case_insensitive: bool = ...,
) -> Callable[[_CoroType], Group[Any]]: ...
@overload
def group(
    name: str = ...,
    *,
    cls: Optional[Type[Group[_CT]]] = ...,
    enabled: bool = ...,
    help: Optional[str] = ...,
    brief: Optional[str] = ...,
    usage: Optional[str] = ...,
    aliases: Union[List[str], Tuple[str, ...]] = ...,
    description: str = ...,
    hidden: bool = ...,
    rest_is_raw: bool = ...,
    ignore_extra: bool = ...,
    cooldown_after_parsing: bool = ...,
    invoke_without_command: bool = ...,
    case_insensitive: bool = ...,
) -> Callable[[_CoroType], Group[Any]]: ...
def check(predicate: _CheckPredicate[_CT]) -> _CheckDecorator: ...
def check_any(*checks: _CheckDecorator) -> _CheckDecorator: ...
def has_role(item: Union[int, str]) -> _CheckDecorator: ...
def has_any_role(*items: Union[int, str]) -> _CheckDecorator: ...
def bot_has_role(item: Union[int, str]) -> _CheckDecorator: ...
def bot_has_any_role(*items: Union[int, str]) -> _CheckDecorator: ...
def has_permissions(**perms: bool) -> _CheckDecorator: ...
def bot_has_permissions(**perms: bool) -> _CheckDecorator: ...
def has_guild_permissions(**perms: bool) -> _CheckDecorator: ...
def bot_has_guild_permissions(**perms: bool) -> _CheckDecorator: ...
def dm_only() -> _CheckDecorator: ...
def guild_only() -> _CheckDecorator: ...
def is_owner() -> _CheckDecorator: ...
def is_nsfw() -> _CheckDecorator: ...
def cooldown(rate: int, per: float, type: _CooldownType = ...) -> _CheckDecorator: ...
def max_concurrency(
    number: int, per: _CooldownType = ..., *, wait: bool = ...
) -> _CheckDecorator: ...
def before_invoke(coro: _InvokeCallback[_CT]) -> _CheckDecorator: ...
def after_invoke(coro: _InvokeCallback[_CT]) -> _CheckDecorator: ...
