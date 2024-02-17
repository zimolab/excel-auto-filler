import dataclasses
import os.path

from PySide2.QtWidgets import QDialog, QButtonGroup, QFileDialog, QMessageBox

from excelfiller_executable.common import DEFAULT_ENCODING, convert_rules_config_file
from excelfiller_executable.gui.generated_code.convert_dialog import Ui_ConvertDialog
from excelfiller_executable.gui.ui.common import RULES_CONFIG_FILE_FILTER

TITLE = "配置文件格式转换"


@dataclasses.dataclass
class _Arguments(object):
    input_file: str
    output_file: str
    encoding: str = DEFAULT_ENCODING
    overwrite: bool = False


class ConvertDialog(QDialog):
    def __init__(self, parent=None):
        super(ConvertDialog, self).__init__(parent)
        self._ui = Ui_ConvertDialog()

        self.setup_ui()
        self.setup_signals()

    def setup_ui(self):
        self._ui.setupUi(self)
        self.setWindowTitle(TITLE)

        self.update_ui_with_arguments(_Arguments(
            input_file="",
            output_file="",
            encoding=DEFAULT_ENCODING,
            overwrite=False
        ))

    def setup_signals(self):
        self._ui.button_start.clicked.connect(self.start_convert)
        self._ui.button_cancel.clicked.connect(self.close)
        self._ui.button_select_input_file.clicked.connect(self.select_input_file)
        self._ui.button_select_output_file.clicked.connect(self.select_output_file)

    def start_convert(self):
        arguments = self.collect_arguments()
        if not arguments.input_file:
            QMessageBox.critical(self, "错误", "请先选择输入文件")
            return
        if not arguments.output_file:
            QMessageBox.critical(self, "错误", "请先选择要保存到的文件")
            return
        if not arguments.encoding:
            QMessageBox.critical(self, "错误", "请先输入有效编码")
            return

        input_path = os.path.abspath(arguments.input_file)
        if not os.path.isfile(input_path):
            QMessageBox.critical(self, "错误", f"文件不存在: {input_path}")
            return

        output_path = os.path.abspath(arguments.output_file)
        if os.path.isfile(output_path) and not arguments.overwrite:
            QMessageBox.critical(self, "错误", f"文件已存在: {output_path}, 且未允许覆盖文件！")
            return

        try:
            convert_rules_config_file(input_file=input_path, output_file=output_path, encoding=arguments.encoding)
        except ValueError as e:
            QMessageBox.critical(self, "错误", f"转换失败，不支持的文件类型: {e}")
            return
        except BaseException as e:
            QMessageBox.critical(self, "错误", f"转换失败，发生一个错误: {e}")
            return
        else:
            QMessageBox.information(self, "成功", f"转换成功, 文件保存到已保存到:{output_path}")

    def select_input_file(self):
        selected_file, _ = QFileDialog.getOpenFileName(self, "选择文件", filter=RULES_CONFIG_FILE_FILTER)
        if not selected_file:
            return
        path = os.path.normcase(os.path.abspath(selected_file))
        if not os.path.isfile(path):
            QMessageBox.information(self, "错误", f"文件不存在: {path}")
            return
        self._ui.edit_input_file.setText(path)

    def select_output_file(self):
        selected_file, _ = QFileDialog.getSaveFileName(self, "保存为", filter=RULES_CONFIG_FILE_FILTER)
        if not selected_file:
            return
        path = os.path.normcase(os.path.abspath(selected_file))
        if os.path.isfile(path) and not self._ui.checkbox_overwrite.isChecked():
            if QMessageBox.question(self, "", "文件已存在，是否覆盖？",
                                    QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                self._ui.checkbox_overwrite.setChecked(True)
                self._ui.edit_output_file.setText(path)
                return
            else:
                return
        self._ui.edit_output_file.setText(path)

    def collect_arguments(self) -> _Arguments:
        input_file = self._ui.edit_input_file.text() or ""
        output_file = self._ui.edit_output_file.text() or ""
        encoding = self._ui.edit_encoding.text() or DEFAULT_ENCODING
        overwrite = self._ui.checkbox_overwrite.isChecked()
        return _Arguments(input_file, output_file, encoding, overwrite)

    def update_ui_with_arguments(self, arguments: _Arguments):
        self._ui.edit_input_file.setText(arguments.input_file)
        self._ui.edit_encoding.setText(arguments.encoding)
        if arguments.overwrite:
            self._ui.checkbox_overwrite.setChecked(True)
        else:
            self._ui.checkbox_overwrite.setChecked(False)
