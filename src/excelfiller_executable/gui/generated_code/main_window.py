# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(957, 691)
        self.action_new_rules_config = QAction(MainWindow)
        self.action_new_rules_config.setObjectName(u"action_new_rules_config")
        self.action_convert = QAction(MainWindow)
        self.action_convert.setObjectName(u"action_convert")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_help = QAction(MainWindow)
        self.action_help.setObjectName(u"action_help")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.groupBox = QGroupBox(self.splitter_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.edit_target_file = QLineEdit(self.groupBox)
        self.edit_target_file.setObjectName(u"edit_target_file")

        self.gridLayout.addWidget(self.edit_target_file, 1, 0, 1, 1)

        self.button_select_target_file = QPushButton(self.groupBox)
        self.button_select_target_file.setObjectName(u"button_select_target_file")

        self.gridLayout.addWidget(self.button_select_target_file, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.edit_save_as_file = QLineEdit(self.groupBox)
        self.edit_save_as_file.setObjectName(u"edit_save_as_file")

        self.gridLayout.addWidget(self.edit_save_as_file, 3, 0, 1, 1)

        self.button_select_save_as_file = QPushButton(self.groupBox)
        self.button_select_save_as_file.setObjectName(u"button_select_save_as_file")

        self.gridLayout.addWidget(self.button_select_save_as_file, 3, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 2)

        self.edit_sheetname = QLineEdit(self.groupBox)
        self.edit_sheetname.setObjectName(u"edit_sheetname")

        self.gridLayout.addWidget(self.edit_sheetname, 5, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)

        self.edit_rules_config_file = QLineEdit(self.groupBox)
        self.edit_rules_config_file.setObjectName(u"edit_rules_config_file")

        self.gridLayout.addWidget(self.edit_rules_config_file, 7, 0, 1, 1)

        self.button_select_rules_config_file = QPushButton(self.groupBox)
        self.button_select_rules_config_file.setObjectName(u"button_select_rules_config_file")

        self.gridLayout.addWidget(self.button_select_rules_config_file, 7, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 2)

        self.edit_encoding = QLineEdit(self.groupBox)
        self.edit_encoding.setObjectName(u"edit_encoding")

        self.gridLayout.addWidget(self.edit_encoding, 9, 0, 1, 1)

        self.checkbox_create = QCheckBox(self.groupBox)
        self.checkbox_create.setObjectName(u"checkbox_create")

        self.gridLayout.addWidget(self.checkbox_create, 10, 0, 1, 2)

        self.checkbox_quick_fail = QCheckBox(self.groupBox)
        self.checkbox_quick_fail.setObjectName(u"checkbox_quick_fail")

        self.gridLayout.addWidget(self.checkbox_quick_fail, 11, 0, 1, 1)

        self.check_overwrite = QCheckBox(self.groupBox)
        self.check_overwrite.setObjectName(u"check_overwrite")

        self.gridLayout.addWidget(self.check_overwrite, 12, 0, 1, 1)

        self.checkbox_save_anyway = QCheckBox(self.groupBox)
        self.checkbox_save_anyway.setObjectName(u"checkbox_save_anyway")

        self.gridLayout.addWidget(self.checkbox_save_anyway, 13, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 195, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 14, 0, 1, 1)

        self.splitter_2.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textbrowser_output = QTextBrowser(self.groupBox_2)
        self.textbrowser_output.setObjectName(u"textbrowser_output")

        self.verticalLayout.addWidget(self.textbrowser_output)

        self.checkbox_clear_output = QCheckBox(self.groupBox_2)
        self.checkbox_clear_output.setObjectName(u"checkbox_clear_output")

        self.verticalLayout.addWidget(self.checkbox_clear_output)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_clear_output = QPushButton(self.groupBox_2)
        self.button_clear_output.setObjectName(u"button_clear_output")

        self.horizontalLayout.addWidget(self.button_clear_output)

        self.button_export_output = QPushButton(self.groupBox_2)
        self.button_export_output.setObjectName(u"button_export_output")

        self.horizontalLayout.addWidget(self.button_export_output)

        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.button_start = QPushButton(self.groupBox_2)
        self.button_start.setObjectName(u"button_start")

        self.horizontalLayout.addWidget(self.button_start)

        self.button_stop = QPushButton(self.groupBox_2)
        self.button_stop.setObjectName(u"button_stop")

        self.horizontalLayout.addWidget(self.button_stop)

        self.button_quit = QPushButton(self.groupBox_2)
        self.button_quit.setObjectName(u"button_quit")

        self.horizontalLayout.addWidget(self.button_quit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.splitter_2.addWidget(self.groupBox_2)

        self.verticalLayout_2.addWidget(self.splitter_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 957, 26))
        self.menu_commands = QMenu(self.menubar)
        self.menu_commands.setObjectName(u"menu_commands")
        self.menu_about = QMenu(self.menubar)
        self.menu_about.setObjectName(u"menu_about")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_commands.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())
        self.menu_commands.addAction(self.action_new_rules_config)
        self.menu_commands.addAction(self.action_convert)
        self.menu_about.addAction(self.action_about)
        self.menu_about.addAction(self.action_help)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("")
        self.action_new_rules_config.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u89c4\u5219\u914d\u7f6e", None))
        self.action_convert.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u6362\u914d\u7f6e\u6587\u4ef6\u683c\u5f0f", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_help.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u6587\u4ef6", None))
        self.button_select_target_file.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a\uff08\u82e5\u4e3a\u7a7a\u5219\u5c06\u7ed3\u679c\u4fdd\u5b58\u5230\u76ee\u6807\u6587\u4ef6\u4e2d\uff09", None))
        self.button_select_save_as_file.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u5de5\u4f5c\u8868\u540d\u79f0\uff08\u82e5\u4e3a\u7a7a\u5219\u4f7f\u7528\u5f53\u524d\u6d3b\u52a8\u5de5\u4f5c\u8868\uff09", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u89c4\u5219\u914d\u7f6e\u6587\u4ef6", None))
        self.button_select_rules_config_file.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u6587\u4ef6\u7f16\u7801\uff08\u9ed8\u8ba4\u4f7f\u7528utf-8\u7f16\u7801\uff09", None))
        self.checkbox_create.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u6587\u4ef6/\u5de5\u4f5c\u8868\u4e0d\u5b58\u5728\u65f6\u81ea\u52a8\u521b\u5efa", None))
        self.checkbox_quick_fail.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u751f\u5f02\u5e38\u65f6\u7acb\u65f6\u7ec8\u6b62\u8fd0\u884c", None))
        self.check_overwrite.setText(QCoreApplication.translate("MainWindow", u"\u5141\u8bb8\u8986\u76d6\u5df2\u5b58\u5728\u7684\u6587\u4ef6", None))
        self.checkbox_save_anyway.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u751f\u5f02\u5e38\u65f6\u4ecd\u4fdd\u5b58\u5f53\u524d\u7ed3\u679c\u4fdd\u5b58\u5230\u76ee\u6807\u6587\u4ef6", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa/\u65e5\u5fd7", None))
        self.checkbox_clear_output.setText(QCoreApplication.translate("MainWindow", u"\u6bcf\u6b21\u5904\u7406\u524d\u6e05\u7a7a\u8f93\u51fa", None))
        self.button_clear_output.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u8f93\u51fa", None))
        self.button_export_output.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u8f93\u51fa", None))
        self.button_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5904\u7406", None))
        self.button_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u5904\u7406", None))
        self.button_quit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.menu_commands.setTitle(QCoreApplication.translate("MainWindow", u"\u547d\u4ee4", None))
        self.menu_about.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

