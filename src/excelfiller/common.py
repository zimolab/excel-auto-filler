import os
import string
from typing import TypeAlias, Any, Iterable, Callable, Tuple

from openpyxl.cell import Cell, MergedCell
from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet

BasicDataType: TypeAlias = str | int | bool | float | list | tuple | dict
PrimitiveDataType: TypeAlias = str | int | bool | float


def is_basic_data_type(value: Any) -> bool:
    return isinstance(value, (str, int, bool, float, list, tuple, dict))


def is_primitive_data_type(value: Any) -> bool:
    return isinstance(value, (str, int, bool, float))


def filetype_from_suffix(path: str, with_dot: bool = False) -> str:
    _, ext = os.path.splitext(path)
    if not with_dot:
        return ext[1:]
    return ext


def flatten(it: Iterable) -> Iterable:
    for item in it:
        if not isinstance(item, (list, tuple)):
            yield item
        else:
            yield from flatten(item)


def determine_values(values_map: dict[str, Callable], *args, **kwargs) -> dict[str, Any]:
    return {k: v(*args, **kwargs) for k, v in values_map.items()}


def get_cells_in_scope(worksheet: Worksheet, scope: str, worksheet_vars: dict[str, Any]) -> Cell | MergedCell | Tuple:
    tpl = string.Template(scope)
    scope = tpl.safe_substitute(worksheet_vars)
    return worksheet[scope]


def get_worksheet(workbook: Workbook, sheet: str | int | None) -> Worksheet:
    if sheet is None:
        return workbook.active
    elif isinstance(sheet, str):
        return workbook[sheet]
    elif isinstance(sheet, int):
        return workbook.worksheets[sheet]
    else:
        raise TypeError(f"sheet must be str or int, got {type(sheet)}")
