import abc
import threading
from typing import Any, Type

import rich.console

from excelfiller.processor import CellRulesProcessor
from excelfiller.rule import CellRulesConfigFactory
from excelfiller_executable.common import BaseCommand

STYLE_ERROR = "red bold"
STYLE_SUCCESS = "green bold"
STYLE_INFO = "bold"
STYLE_WARN = "yellow bold"
STYLE_HINT = "blue bold"


class CLICommand(BaseCommand):
    def __init__(self, cli: "CellRulesProcessorCLI", *args, **kwargs):
        self.cli = cli

    @abc.abstractmethod
    def run(self, *args, **kwargs):
        pass


class CellRulesProcessorCLI(object):
    def __init__(self):
        self._lock = threading.Lock()
        self._console = rich.console.Console()
        self._cell_rules_processor = CellRulesProcessor()
        self._cell_rules_config_factory = CellRulesConfigFactory()

    @property
    def console(self):
        return self._console

    @property
    def rules_processor(self) -> CellRulesProcessor:
        return self._cell_rules_processor

    @property
    def rules_config_factory(self) -> CellRulesConfigFactory:
        return self._cell_rules_config_factory

    def print(self, *objects: Any, **kwargs):
        with self._lock:
            self._console.print(*objects, **kwargs)

    def run_command(self, command: CLICommand, *args, **kwargs):
        try:
            command.run(*args, **kwargs)
        except BaseException as e:
            self.print(f"[Error]: Failed to run command:{command}:{e}", style=STYLE_ERROR)
            self.print_exception()

    def print_exception(self, *args, **kwargs):
        with self._lock:
            self._console.print_exception(*args, **kwargs)
