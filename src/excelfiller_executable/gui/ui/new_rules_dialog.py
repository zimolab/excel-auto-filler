import dataclasses
import os

from PySide2.QtWidgets import QDialog, QButtonGroup, QFileDialog, QMessageBox

from excelfiller_executable.common import DEFAULT_ENCODING, new_rules_config_file
from excelfiller_executable.gui.generated_code.new_rules_dialog import Ui_NewRulesConfigDialog
from excelfiller_executable.gui.ui.common import RULES_CONFIG_FILE_FILTER

TITLE = "创建规则配置文件"


@dataclasses.dataclass
class _Arguments(object):
    target_file: str
    encoding: str = DEFAULT_ENCODING
    overwrite: bool = False
    human: bool = True


class NewRulesConfigDialog(QDialog):
    def __init__(self, parent=None):
        super(NewRulesConfigDialog, self).__init__(parent)
        self._ui = Ui_NewRulesConfigDialog()

        self.setup_ui()
        self.setup_signals()

    def setup_ui(self):
        self._ui.setupUi(self)
        self.setWindowTitle(TITLE)

        group = QButtonGroup(self)
        group.addButton(self._ui.radio_human)
        group.addButton(self._ui.radio_nonhuman)

        self.update_ui_with_arguments(_Arguments(
            target_file="",
            encoding=DEFAULT_ENCODING,
            overwrite=False,
            human=True
        ))

    def setup_signals(self):
        self._ui.button_cancel.clicked.connect(self.close)
        self._ui.button_start.clicked.connect(self.new_rules_config_file)
        self._ui.button_select_target_file.clicked.connect(self.select_target_file)

    def new_rules_config_file(self):
        arguments = self.collect_arguments()
        path = os.path.abspath(arguments.target_file)
        if not arguments.overwrite and os.path.isfile(path):
            QMessageBox.critical(self, "错误", f"文件已存在: {path}, 且未允许覆盖文件！")
            return
        try:
            new_rules_config_file(path, arguments.encoding, arguments.human)
        except BaseException as e:
            QMessageBox.critical(self, "错误", f"创建规则配置文件失败: {e}")
        else:
            QMessageBox.information(self, "成功", f"创建规则配置文件成功: {path}")

    def select_target_file(self):
        selected_file, _ = QFileDialog.getSaveFileName(self, "选择文件", filter=RULES_CONFIG_FILE_FILTER)
        if not selected_file:
            return
        path = os.path.normcase(os.path.abspath(selected_file))
        if os.path.isfile(path) and not self._ui.checkbox_overwrite.isChecked():
            if QMessageBox.question(self, "", "文件已存在，是否覆盖？",
                                    QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
                self._ui.checkbox_overwrite.setChecked(True)
                self._ui.edit_target_file.setText(path)
                return
            else:
                return
        self._ui.edit_target_file.setText(path)

    def collect_arguments(self) -> _Arguments:
        return _Arguments(
            target_file=self._ui.edit_target_file.text() or "",
            encoding=self._ui.edit_encoding.text() or DEFAULT_ENCODING,
            overwrite=self._ui.checkbox_overwrite.isChecked(),
            human=self._ui.radio_human.isChecked()
        )

    def update_ui_with_arguments(self, arguments: _Arguments):
        self._ui.edit_target_file.setText(arguments.target_file)
        self._ui.edit_encoding.setText(arguments.encoding)
        self._ui.checkbox_overwrite.setChecked(arguments.overwrite)
        self._ui.radio_human.setChecked(arguments.human)
        self._ui.radio_nonhuman.setChecked(not arguments.human)
