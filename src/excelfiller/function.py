import abc
import dataclasses
from typing import Any, Iterable, TypeAlias, Callable

from openpyxl.cell import Cell, MergedCell
from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from excelfiller.common import get_cells_in_scope, flatten, BasicDataType


class NULL(object):
    pass


# 关于参数的说明：第一个参数代表当前正在遍历的单元格
# 关于返回值的说明：返回值代表是否需要停止遍历，返回值为True时，停止遍历下一个单元格
WalkCallback: TypeAlias = Callable[[Cell | MergedCell], bool]


@dataclasses.dataclass
class FunctionContext(object):
    # 当前规则的范围，来源于当前CellRule的scope属性
    rule_scope: str
    # CellRulesConfig中定义的一些全局变量（对所有规则可见，因此会被拷贝到每个规则对应函数的上下文中）
    rules_globals: dict[str, BasicDataType]
    # 当前工作簿
    workbook: Workbook
    # 当前工作表
    worksheet: Worksheet
    # 当前工作表的一些变量
    worksheet_vars: dict[str, Any]

    def walk_cells_in_scope(self, callback: WalkCallback, flatten_cells: bool = True):
        cells = self.get_cells_in_scope()
        if flatten_cells:
            cells = flatten(cells)
        for cell in cells:
            stop_walking = callback(cell)
            if stop_walking:
                break

    def get_cells_in_scope(self) -> Iterable[Cell | MergedCell]:
        return get_cells_in_scope(self.worksheet, self.rule_scope, self.worksheet_vars)


class BaseFunction(abc.ABC):
    @property
    @abc.abstractmethod
    def context(self) -> FunctionContext | None:
        pass

    @property
    @abc.abstractmethod
    def current_cell(self) -> Cell | MergedCell | None:
        pass

    @abc.abstractmethod
    def before_invoke(self, context: FunctionContext | None, current_cell: Cell | MergedCell | None):
        pass

    @abc.abstractmethod
    def on_invoke(self, *args, **kwargs) -> Any:
        pass

    @abc.abstractmethod
    def after_invoke(self):
        pass

    def invoke(self, context: FunctionContext | None, current_cell: Cell | MergedCell | None, /,  *args, **kwargs) -> Any:
        self.before_invoke(context, current_cell)
        try:
            result = self.on_invoke(*args, **kwargs)
            return result
        except BaseException as e:
            raise e
        finally:
            self.after_invoke()


class ContextAwareFunction(BaseFunction):

    def __init__(self):
        self._context = None
        self._current_cell = None

    @property
    def context(self) -> FunctionContext | None:
        return self._context

    @property
    def current_cell(self) -> Cell | MergedCell | None:
        return self._current_cell

    def before_invoke(self, context: FunctionContext | None, current_cell: Cell | MergedCell | None):
        self._context = context
        self._current_cell = current_cell

    @abc.abstractmethod
    def on_invoke(self, *args, **kwargs) -> Any:
        pass

    def after_invoke(self):
        self._context = None
        self._current_cell = None


class ContextFreeFunction(BaseFunction):

    @property
    def context(self) -> FunctionContext | None:
        return None

    @property
    def current_cell(self) -> Cell | MergedCell | None:
        return None

    def before_invoke(self, context: FunctionContext, current_cell: Cell | MergedCell | None):
        pass

    def after_invoke(self):
        pass

    @abc.abstractmethod
    def on_invoke(self, *args, **kwargs) -> Any:
        pass
