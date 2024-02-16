# 单元格自动填充工具

```text
Excel Automatic Filler
    Fill a worksheet with certain rules defined by the user.
Usage:
    excelfiller run --rules-config=<file> [--verbose] [--encoding=<encoding>] [--sheet=<sheet>] [--create] [--run-async] [--quick-fail] [--save-as=<file>] [--overwrite] [--save-anyway] <target_file>
    excelfiller (-h | --help)
    excelfiller --version
    excelfiller gui
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
```