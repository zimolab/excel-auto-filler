from typing import Any

from PySide2.QtCore import QObject
from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from excelfiller.common import PrimitiveDataType
from excelfiller.function import FunctionContext
from excelfiller.rule import CellRulesConfig, CellRule
from excelfiller_executable.common import description_of_rule


# noinspection PyUnusedLocal
class _ProcessorEventHandler(QObject):
    def __init__(self, parent: QObject):
        super().__init__(parent)
        self._target = None
        self._state_total_items = 0
        self._state_current_item = 0

    # noinspection PyUnresolvedReferences
    def takeover(self, target: "RuleProcessorWindow"):
        if target and target != self._target:
            self._target = target
            controller = self._target.processing_controller
            controller.processing_started.connect(self.on_processing_started)
            controller.processing_finished.connect(self.on_processing_finished)
            controller.processing_errored.connect(self.on_processing_errored)
            controller.before_rule_executed.connect(self.before_rule_executed)
            controller.rule_execution_succeeded.connect(self.on_rule_execution_succeeded)
            controller.rule_execution_failed.connect(self.on_rule_execution_failed)

    # noinspection PyUnresolvedReferences
    def release(self):
        if self._target:
            controller = self._target.processing_controller
            controller.processing_started.disconnect(self.on_processing_started)
            controller.processing_finished.disconnect(self.on_processing_finished)
            controller.processing_errored.disconnect(self.on_processing_errored)
            controller.before_rule_executed.disconnect(self.on_before_rule_executed)
            controller.rule_execution_succeeded.disconnect(self.on_rule_execution_succeeded)
            controller.rule_execution_failed.disconnect(self.on_rule_execution_failed)
            self._target = None

    def on_processing_started(self, workbook: Workbook, worksheet: Worksheet, rules_config: CellRulesConfig):
        if not self._target:
            return
        self._state_total_items = len(rules_config.rules)
        self._state_current_item = 1

        if self._target.is_clear_output_before_start():
            self._target.clear_output()

        self._target.output_info(f"开始处理")
        self._target.output_info(f"共有<b><font color=white>{len(rules_config.rules)}</font></b>项待处理规则项",
                                 additional_nl=True)

    def on_processing_finished(self, workbook: Workbook, worksheet: Worksheet, rules_config: CellRulesConfig,
                               error: BaseException | None):
        self._state_total_items = 0
        self._state_current_item = 0
        if not self._target:
            return
        if error:
            self._target.output_critical("处理过程中发生异常")
            self._target.output_fatal(f"异常信息：{error}")
        self._target.output_info("处理完成")
        self._target.ui.button_start.setEnabled(True)

    def on_processing_errored(self, workbook: Workbook, worksheet: Worksheet, rules_config: CellRulesConfig,
                              error: BaseException):
        if not self._target:
            return

        self._target.output_critical("处理过程中发生异常")
        self._target.output_fatal(f"异常信息：{error}")

    def before_rule_executed(self, context: FunctionContext, rule_scope_target: CellRule | PrimitiveDataType | list):
        if not self._target:
            return
        if isinstance(rule_scope_target, list):
            rule_count = len(rule_scope_target)
        else:
            rule_count = 1

        self._target.output_info(
            f"即将执行<b><font color=white>[{self._state_current_item}/{self._state_total_items}]</font></b>规则项")
        self._target.output_debug(f"规则项范围为<b>{context.rule_scope}<b>, 共<b>{rule_count}</b>条规则")
        self._state_current_item += 1

    def on_rule_execution_succeeded(self, context: FunctionContext, rule: CellRule | PrimitiveDataType, result: Any):
        if not self._target:
            return
        self._target.output_info(f"规则执行成功")
        self._target.output_debug(f"规则范围：<b>{context.rule_scope}</b>")
        self._target.output_debug(f"规则内容：{description_of_rule(rule)}")
        self._target.output_debug(f"执行结果：<b><font color=white>{result}</font></b>", additional_nl=True)

    def on_rule_execution_failed(self, context: FunctionContext, rule: CellRule | PrimitiveDataType,
                                 error: BaseException):
        if not self._target:
            return
        self._target.output_critical(f"规则执行失败")
        self._target.output_debug(f"规则范围：<b>{context.rule_scope}</b>")
        self._target.output_debug(f"规则内容：{description_of_rule(rule)}")
        self._target.output_fatal(f"异常信息：{error}", additional_nl=True)
