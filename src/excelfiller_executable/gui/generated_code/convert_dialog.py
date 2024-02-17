# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'convert_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ConvertDialog(object):
    def setupUi(self, ConvertDialog):
        if not ConvertDialog.objectName():
            ConvertDialog.setObjectName(u"ConvertDialog")
        ConvertDialog.resize(477, 199)
        self.verticalLayout = QVBoxLayout(ConvertDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_select_input_file = QPushButton(ConvertDialog)
        self.button_select_input_file.setObjectName(u"button_select_input_file")

        self.gridLayout.addWidget(self.button_select_input_file, 0, 5, 1, 1)

        self.button_start = QPushButton(ConvertDialog)
        self.button_start.setObjectName(u"button_start")

        self.gridLayout.addWidget(self.button_start, 4, 5, 1, 1)

        self.label_3 = QLabel(ConvertDialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.edit_encoding = QLineEdit(ConvertDialog)
        self.edit_encoding.setObjectName(u"edit_encoding")

        self.gridLayout.addWidget(self.edit_encoding, 2, 1, 1, 4)

        self.checkbox_overwrite = QCheckBox(ConvertDialog)
        self.checkbox_overwrite.setObjectName(u"checkbox_overwrite")

        self.gridLayout.addWidget(self.checkbox_overwrite, 3, 0, 1, 5)

        self.edit_output_file = QLineEdit(ConvertDialog)
        self.edit_output_file.setObjectName(u"edit_output_file")

        self.gridLayout.addWidget(self.edit_output_file, 1, 1, 1, 4)

        self.button_cancel = QPushButton(ConvertDialog)
        self.button_cancel.setObjectName(u"button_cancel")

        self.gridLayout.addWidget(self.button_cancel, 4, 4, 1, 1)

        self.label_4 = QLabel(ConvertDialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.label_2 = QLabel(ConvertDialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.button_select_output_file = QPushButton(ConvertDialog)
        self.button_select_output_file.setObjectName(u"button_select_output_file")

        self.gridLayout.addWidget(self.button_select_output_file, 1, 5, 1, 1)

        self.edit_input_file = QLineEdit(ConvertDialog)
        self.edit_input_file.setObjectName(u"edit_input_file")

        self.gridLayout.addWidget(self.edit_input_file, 0, 1, 1, 4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 0, 1, 4)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(ConvertDialog)

        QMetaObject.connectSlotsByName(ConvertDialog)
    # setupUi

    def retranslateUi(self, ConvertDialog):
        ConvertDialog.setWindowTitle(QCoreApplication.translate("ConvertDialog", u"Dialog", None))
        self.button_select_input_file.setText(QCoreApplication.translate("ConvertDialog", u"\u9009\u62e9\u6587\u4ef6", None))
        self.button_start.setText(QCoreApplication.translate("ConvertDialog", u"\u5f00\u59cb\u8f6c\u6362", None))
        self.label_3.setText(QCoreApplication.translate("ConvertDialog", u"\u4fdd\u5b58\u4e3a", None))
        self.checkbox_overwrite.setText(QCoreApplication.translate("ConvertDialog", u"\u5141\u8bb8\u8986\u76d6\u5df2\u5b58\u5728\u7684\u6587\u4ef6", None))
        self.button_cancel.setText(QCoreApplication.translate("ConvertDialog", u"\u53d6\u6d88", None))
        self.label_4.setText(QCoreApplication.translate("ConvertDialog", u"\u6587\u4ef6\u7f16\u7801", None))
        self.label_2.setText(QCoreApplication.translate("ConvertDialog", u"\u8f93\u5165\u6587\u4ef6", None))
        self.button_select_output_file.setText(QCoreApplication.translate("ConvertDialog", u"\u9009\u62e9\u6587\u4ef6", None))
    # retranslateUi

