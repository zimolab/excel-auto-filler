# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_rules_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NewRulesConfigDialog(object):
    def setupUi(self, NewRulesConfigDialog):
        if not NewRulesConfigDialog.objectName():
            NewRulesConfigDialog.setObjectName(u"NewRulesConfigDialog")
        NewRulesConfigDialog.resize(480, 272)
        self.verticalLayout = QVBoxLayout(NewRulesConfigDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(NewRulesConfigDialog)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.edit_target_file = QLineEdit(NewRulesConfigDialog)
        self.edit_target_file.setObjectName(u"edit_target_file")

        self.horizontalLayout_2.addWidget(self.edit_target_file)

        self.button_select_target_file = QPushButton(NewRulesConfigDialog)
        self.button_select_target_file.setObjectName(u"button_select_target_file")

        self.horizontalLayout_2.addWidget(self.button_select_target_file)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(NewRulesConfigDialog)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.edit_encoding = QLineEdit(NewRulesConfigDialog)
        self.edit_encoding.setObjectName(u"edit_encoding")

        self.horizontalLayout_3.addWidget(self.edit_encoding)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.checkbox_overwrite = QCheckBox(NewRulesConfigDialog)
        self.checkbox_overwrite.setObjectName(u"checkbox_overwrite")

        self.verticalLayout.addWidget(self.checkbox_overwrite)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radio_human = QRadioButton(NewRulesConfigDialog)
        self.radio_human.setObjectName(u"radio_human")

        self.horizontalLayout_4.addWidget(self.radio_human)

        self.radio_nonhuman = QRadioButton(NewRulesConfigDialog)
        self.radio_nonhuman.setObjectName(u"radio_nonhuman")

        self.horizontalLayout_4.addWidget(self.radio_nonhuman)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.button_cancel = QPushButton(NewRulesConfigDialog)
        self.button_cancel.setObjectName(u"button_cancel")

        self.horizontalLayout.addWidget(self.button_cancel)

        self.button_start = QPushButton(NewRulesConfigDialog)
        self.button_start.setObjectName(u"button_start")

        self.horizontalLayout.addWidget(self.button_start)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(NewRulesConfigDialog)

        QMetaObject.connectSlotsByName(NewRulesConfigDialog)
    # setupUi

    def retranslateUi(self, NewRulesConfigDialog):
        NewRulesConfigDialog.setWindowTitle(QCoreApplication.translate("NewRulesConfigDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("NewRulesConfigDialog", u"\u76ee\u6807\u6587\u4ef6", None))
        self.button_select_target_file.setText(QCoreApplication.translate("NewRulesConfigDialog", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("NewRulesConfigDialog", u"\u6587\u4ef6\u7f16\u7801", None))
        self.checkbox_overwrite.setText(QCoreApplication.translate("NewRulesConfigDialog", u"\u5141\u8bb8\u8986\u76d6\u5df2\u5b58\u5728\u7684\u6587\u4ef6", None))
        self.radio_human.setText(QCoreApplication.translate("NewRulesConfigDialog", u"\u8bf4\u4eba\u8bdd\u7248\u672c", None))
        self.radio_nonhuman.setText(QCoreApplication.translate("NewRulesConfigDialog", u"\u80e1\u8a00\u4e71\u8bed\u7248", None))
        self.button_cancel.setText(QCoreApplication.translate("NewRulesConfigDialog", u"\u53d6\u6d88", None))
        self.button_start.setText(QCoreApplication.translate("NewRulesConfigDialog", u"\u521b\u5efa\u6587\u4ef6", None))
    # retranslateUi

