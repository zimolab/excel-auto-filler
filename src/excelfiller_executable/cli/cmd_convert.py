import os.path

from excelfiller.rule import CellRulesConfigFactory
from excelfiller_executable.cli.cli import CLICommand, CellRulesProcessorCLI, STYLE_ERROR
from excelfiller_executable.common import DEFAULT_ENCODING


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

        factory = CellRulesConfigFactory()
        input_config = factory.load(path=self.input_file, encoding=self.encoding)
        output_filetype = factory.get_filetype(self.output_file)
        output_config_type = factory.get(output_filetype)
        if not output_config_type:
            self.cli.print(f"[Error] output file type not supported: {output_filetype}", style=STYLE_ERROR)
            return
        output_config = output_config_type.from_object(input_config.as_object())
        output_config.save(filepath=self.output_file, encoding=self.encoding)

