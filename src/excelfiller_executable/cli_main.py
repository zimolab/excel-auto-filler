"""Excel Automatic Filler
    Fill a worksheet with certain rules defined by the user.
Usage:
    excelfiller run --rules-config=<file> [--verbose] [--encoding=<encoding>] [--sheet=<sheet>] [--create] [--run-async] [--quick-fail] [--save-as=<file>] [--overwrite] [--save-anyway] <target_file>
    excelfiller (-h | --help)
    excelfiller --version
    excelfiller new rules-config [--encoding=<encoding>] [--overwrite] [--human] <config_file>
    excelfiller convert [--encoding=<encoding>] [--overwrite] <input_file> <output_file>

Options:
    -h --help                     Show help information.
    --version                     Show version.
    --sheet=<sheet>               Target worksheet name.
    --rules-config=<file>         File path to the rules config file.
    --encoding=<encoding>         The encoding of the rules config file. Default to utf-8
    --create                      Whether to create the target file and worksheet while the target file or worksheet does not exist.
    --quick-fail                  Whether to stop running while an error occurred.
    --run-async                   Run rules in an async way
    --save-as=<file>              Save the workbook to a new file, make sure this file does not exist.
    --overwrite                   Whether to overwrite the existing file.
    --save-anyway                 Ignore errors and save file anyway
    --verbose                     Whether to display detailed output information
    --human                       Use human friendly template.
"""
import sys

from docopt import docopt

from excelfiller_executable.cli.cli import CellRulesProcessorCLI
from excelfiller_executable.cli.cmd_config import CommandNewRulesConfig
from excelfiller_executable.cli.cmd_run import CommandRunRules
from excelfiller_executable.cli.cmd_convert import CommandConvert
from excelfiller_executable.common import DEFAULT_ENCODING

CLI_VERSION = "0.1.0"


def main():
    arguments = docopt(__doc__, version=CLI_VERSION)
    processor_cli = CellRulesProcessorCLI()
    if arguments["convert"]:
        input_file = arguments["<input_file>"] or ""
        output_file = arguments["<output_file>"] or ""
        encoding = arguments["--encoding"] or DEFAULT_ENCODING
        overwrite = arguments["--overwrite"] or False

        command = CommandConvert(processor_cli, input_file=input_file, output_file=output_file, encoding=encoding,
                                 overwrite=overwrite)
        processor_cli.run_command(command)
        return

    if arguments["new"] and arguments["rules-config"]:
        path = arguments["<config_file>"] or ""
        encoding = arguments["--encoding"] or DEFAULT_ENCODING
        overwrite = arguments["--overwrite"] or False
        human = arguments["--human"] or False

        command = CommandNewRulesConfig(processor_cli, path=path, encoding=encoding, overwrite=overwrite, human=human)
        processor_cli.run_command(command)
        return

    if arguments["run"]:
        config_file = arguments["--rules-config"] or ""
        config_file_encoding = arguments["--encoding"] or DEFAULT_ENCODING
        target_xlsx = arguments["<target_file>"] or ""
        sheet = arguments["--sheet"] or None
        create = arguments["--create"] or False
        save_as = arguments["--save-as"] or None
        run_async = arguments["--run-async"] or False
        quick_fail = arguments["--quick-fail"] or False
        overwrite = arguments["--overwrite"] or False
        save_anyway = arguments["--save-anyway"] or False
        verbose = arguments["--verbose"] or False

        command = CommandRunRules(processor_cli, config_file=config_file, config_file_encoding=config_file_encoding,
                                  target_xlsx=target_xlsx, sheet=sheet, create=create, save_as=save_as,
                                  run_async=run_async, quick_fail=quick_fail, overwrite=overwrite,
                                  save_anyway=save_anyway, verbose=verbose)
        processor_cli.run_command(command)
        return


if __name__ == '__main__':
    main()
