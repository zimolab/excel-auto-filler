# try:
#     import ctypes
#     ctypes.windll.shcore.SetProcessDpiAwareness(2)
# except BaseException as e:
#     pass
#
# from gooey import Gooey, GooeyParser
# from excelfiller_executable.gui.cmd_newconfig import CommandNewRulesConfigFile
#
# PROG_NAME = "Excel表格自动填充器"
# PROG_VER = "0.1.0"
# LANG = "Chinese"
# DESCRPIPTION = "Excel工作表自动填充工具——使用规则配置文件填充工作表。"
#
#
# @Gooey(required_cols=1, optional_cols=2, program_name=PROG_NAME, language=LANG)
# def main():
#     parser = GooeyParser(description=DESCRPIPTION)
#     subs = parser.add_subparsers(help="", dest='command')
#     CommandNewRulesConfigFile.create_parser(subs)
#     sub_parser = subs.add_parser("RUN", help="新建规则配置文件")
#     parser.parse_args()
#
#
# if __name__ == '__main__':
#     main()
