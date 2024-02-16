import abc
import os.path
import sys

from openpyxl.workbook import Workbook

from rich.console import Console

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
