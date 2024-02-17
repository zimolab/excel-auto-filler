import os.path

from excelfiller_executable.cli.cli import CLICommand, CellRulesProcessorCLI, STYLE_ERROR
from excelfiller_executable.common import DEFAULT_ENCODING, convert_rules_config_file


class CommandConvert(CLICommand):
    def __init__(self, cli: CellRulesProcessorCLI, input_file: str, output_file: str, encoding: str, overwrite: bool = False):
        super().__init__(cli)

        self.input_file = input_file
        self.output_file = output_file
        self.encoding = encoding or DEFAULT_ENCODING
        self.overwrite = overwrite

    def run(self, *args, **kwargs):
        if not os.path.isfile(self.input_file):
            self.cli.print(f"[Error]File not found: {self.input_file}", style=STYLE_ERROR)
            return

        if os.path.isfile(self.output_file) and not self.overwrite:
            self.cli.print(f"[Error]File '{self.output_file}' already exists, use --overwrite to overwrite it ",
                           style=STYLE_ERROR)
            return
        try:
            convert_rules_config_file(input_file=self.input_file, output_file=self.output_file, encoding=self.encoding)
        except ValueError as e:
            self.cli.print(f"[Error] {e}")
        except BaseException as e:
            self.cli.print(f"[Error] {e}")
            self.cli.print_exception()



