from PySide2.QtCore import Qt
from PySide2.QtWidgets import QDialog, QLabel, QVBoxLayout, QDialogButtonBox

from excelfiller_executable.gui.ui.common import PROG_NAME, VERSION, AUTHOR, WEBSITE, CONTACT

ABOUT_TEXT = f"""
    <h3>{PROG_NAME}</h3>
    版本: {VERSION}<br/>
    开发者: {AUTHOR} <br/>
    网址: {WEBSITE}<br/>
    邮件: {CONTACT}<br/>
    协议: MIT
    <p>版权所有 © 2024 {AUTHOR}. All rights reserved.</p>
"""

TITLE = "关于本程序"


class AboutDialog(QDialog):
    # noinspection PyUnresolvedReferences
    def __init__(self, parent=None):
        super().__init__(parent)

        # 设置对话框标题
        self.setWindowTitle(TITLE)

        # 创建垂直布局
        layout = QVBoxLayout()

        # 创建一个标签显示应用的基本信息
        about_label = QLabel(ABOUT_TEXT)
        about_label.setTextFormat(Qt.RichText)  # 允许HTML格式化文本
        layout.addWidget(about_label)

        # 添加底部按钮（例如关闭按钮）
        button_box = QDialogButtonBox(QDialogButtonBox.Ok)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)

        # 设置对话框的主布局
        self.setLayout(layout)
