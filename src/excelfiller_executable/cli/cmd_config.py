import os
import shutil

from excelfiller.rule import CellRulesConfig, CellRule, CellRulesConfigFactory
from excelfiller_executable.cli.cli import CLICommand, CellRulesProcessorCLI, STYLE_ERROR
from excelfiller_executable.common import get_data_file_path, DEFAULT_ENCODING


class CommandNewRulesConfig(CLICommand):
    def __init__(self, cli: "CellRulesProcessorCLI", path: str, encoding: str, overwrite: bool = False, human: bool = False):
        super().__init__(cli)
        self.path = path
        self.encoding = encoding or DEFAULT_ENCODING
        self.overwrite = overwrite
        self.human = human

    @staticmethod
    def add_demo_rules(rules_config: CellRulesConfig):
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

    def run(self, *args, **kwargs):

        if os.path.exists(self.path) and not self.overwrite:
            self.cli.print(f"[Error] File '{self.path}' already exists, "
                           f"use --overwrite to overwrite it", style=STYLE_ERROR)
            return

        filetype = CellRulesConfigFactory.get_filetype(self.path)
        if self.human:
            filename = f"human.{filetype}"
            human_template = get_data_file_path(filename)
            print(os.path.abspath(human_template))
            if os.path.isfile(human_template):
                shutil.copy(human_template, self.path)
                return

        factory = self.cli.rules_config_factory
        rules_config = factory.create(factory.get_filetype(self.path))
        self.add_demo_rules(rules_config)
        rules_config.save(filepath=self.path, encoding=self.encoding)
