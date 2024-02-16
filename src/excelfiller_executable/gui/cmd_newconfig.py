# """
# excelfiller new rules-config [--encoding=<encoding>] [--overwrite] [--human] <config_file>
# """
# from excelfiller_executable import BaseCommand
#
# DEFAULT_ENCODING = "utf-8"
#
#
# class CommandNewRulesConfigFile(BaseCommand):
#     def __init__(self, config_file: str, encoding: str = DEFAULT_ENCODING, overwrite: bool = False, human: bool = True):
#         self.config_file = config_file
#         self.encoding = encoding or DEFAULT_ENCODING
#         self.overwrite = overwrite
#         self.human = human
#
#     @classmethod
#     def create_parser(cls, subparsers):
#         sub_parser = subparsers.add_parser("new-rules-config", help="新建规则配置文件")
#         sub_parser.add_argument("config-file", help="规则配置文件", type=str, widget="FileChooser")
#         sub_parser.add_argument("--overwrite", help="是否覆盖已存在的文件", type=bool, default=False, widget="CheckBox")
#         sub_parser.add_argument("--encoding",help=f"文件编码格式（默认为{DEFAULT_ENCODING}）", type=str, default=DEFAULT_ENCODING)
#         return sub_parser
#
#     def run(self):
#         pass
