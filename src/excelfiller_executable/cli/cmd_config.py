import os

from excelfiller_executable.cli.cli import CLICommand, CellRulesProcessorCLI, STYLE_ERROR
from excelfiller_executable.common import DEFAULT_ENCODING, new_rules_config_file


class CommandNewRulesConfig(CLICommand):
    def __init__(self, cli: "CellRulesProcessorCLI", path: str, encoding: str, overwrite: bool = False, human: bool = False):
        super().__init__(cli)
        self.path = path
        self.encoding = encoding or DEFAULT_ENCODING
        self.overwrite = overwrite
        self.human = human

    def run(self, *args, **kwargs):

        if os.path.exists(self.path) and not self.overwrite:
            self.cli.print(f"[Error] File '{self.path}' already exists, "
                           f"use --overwrite to overwrite it", style=STYLE_ERROR)
            return

        try:
            new_rules_config_file(self.path, self.encoding, self.human)
        except BaseException as e:
            self.cli.print(f"[Error] Failed to create rules config file '{self.path}': {e}")
            self.cli.print_exception()

