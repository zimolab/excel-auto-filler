import abc
import os.path
import shutil
import sys

from openpyxl.workbook import Workbook

from rich.console import Console

from excelfiller.common import PrimitiveDataType
from excelfiller.rule import CellRule, CellRulesConfigFactory

_console = Console()

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))
DEFAULT_ENCODING = "utf-8"
DEFAULT_QUICK_FAIL = False
DEFAULT_HUMAN = True


class BaseCommand(abc.ABC):
    @abc.abstractmethod
    def run(self, *args, **kwargs):
        pass


def create_xlsx_file(path: str):
    new_workbook = Workbook()
    new_workbook.save(filename=path)
    return new_workbook


def get_data_dir() -> str:
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, "data")
    else:
        return DATA_DIR


def get_data_file_path(path: str) -> str:
    return os.path.join(get_data_dir(), path)


def description_of_rule(rule: CellRule | PrimitiveDataType) -> str:
    if isinstance(rule, CellRule):
        return f"result={rule.fn}(*args, **kwargs, pre_cell={rule.per_cell})"
    else:
        return f"result={rule}"


def convert_rules_config_file(input_file: str, output_file: str, encoding: str, overwrite: bool = False):
    factory = CellRulesConfigFactory()
    input_config = factory.load(path=input_file, encoding=encoding)
    output_filetype = factory.get_filetype(output_file)
    output_config_type = factory.get(output_filetype)
    if not output_config_type:
        raise ValueError(f"output file type not supported: {output_filetype}")

    output_config = output_config_type.from_object(input_config.as_object())
    output_config.save(filepath=output_file, encoding=encoding)


def _add_demo_rules(rules_config):
    # rules_globals demo
    rules_config.rules_globals["g_var"] = ("this var can be accessed in ContextAwareFunction "
                                           "via context.rules_globals['g_var']")
    # rules demo
    # rule可以是单个PrimitiveDataType值，scope可以是指定单元格
    rules_config.rules["A1"] = "single primitive value"
    # rule也可以是单个CellRule，scope可以是指定的行或列
    rules_config.rules["B"] = CellRule(fn="random", args=["randint", 20, 65])
    # rule也可以是多个CellRule组成的列表，scope可以是指定的单元格范围，且可以使用$MAX_COL, $MAX_ROW, $MIN_COL, $MIN_ROW等变量
    rules_config.rules["C$MIN_ROW:F$MAX_ROW"] = [
        CellRule(fn="random", args=["randint", 20, 65]),
        CellRule(fn="random", args=["choice", ("boy", "girl")]),
        CellRule(fn="fake", args=["name"]),
    ]


def new_rules_config_file(path: str, encoding: str, human: bool = False):
    filetype = CellRulesConfigFactory.get_filetype(path)
    if human:
        filename = f"human.{filetype}"
        human_template = get_data_file_path(filename)
        if os.path.isfile(human_template):
            shutil.copy(human_template, path)
            return

    factory = CellRulesConfigFactory()
    rules_config = factory.create(factory.get_filetype(path))
    _add_demo_rules(rules_config)
    rules_config.save(filepath=path, encoding=encoding)