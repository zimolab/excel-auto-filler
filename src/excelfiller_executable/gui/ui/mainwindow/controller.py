import os
from typing import Any, List

from PySide2.QtCore import QObject, Signal
from openpyxl.workbook import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from excelfiller.common import PrimitiveDataType
from excelfiller.function import FunctionContext
from excelfiller.processor import CellRulesProcessor
from excelfiller.rule import CellRulesConfig, CellRulesConfigFactory, CellRule


class CellRulesProcessingController(QObject):
    processing_started = Signal(Workbook, Worksheet, CellRulesConfig)
    processing_finished = Signal(Workbook, Worksheet, CellRulesConfig, BaseException)
    processing_errored = Signal(Workbook, Worksheet, CellRulesConfig, BaseException)
    before_rule_executed = Signal(FunctionContext, object)
    rule_execution_succeeded = Signal(FunctionContext, object, object)
    rule_execution_failed = Signal(FunctionContext, object, BaseException)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._processor = CellRulesProcessor()

        self._current_arg_save_path = ""
        self._current_arg_overwrite = None
        self._current_arg_save_anyway = None
        self._current_state_exception = None

        self._config_factory = CellRulesConfigFactory()

        self._processor.processing_started.connect(self._on_started)
        self._processor.processing_finished.connect(self._on_finished)
        self._processor.processing_errored.connect(self._on_processing_errored)
        self._processor.rule_execution_succeed.connect(self._on_succeed)
        self._processor.rule_execution_failed.connect(self._on_failed)
        self._processor.before_rule_executed.connect(self._before_executed)

    def start_processing(self, workbook: Workbook, worksheet: Worksheet, rules_config: CellRulesConfig,
                         save_path: str, overwrite: bool, save_anyway: bool, quick_fail: bool):
        if self._processor.is_processing():
            return

        self._reset_state()

        self._current_arg_save_path = save_path
        self._current_arg_overwrite = overwrite
        self._current_arg_save_anyway = save_anyway
        self._current_state_exception = None

        self._processor.process_async(
            workbook=workbook,
            worksheet=worksheet,
            rules_config=rules_config,
            quick_fail=quick_fail,
        )

    def stop_processing(self):
        if not self._processor.is_processing():
            return
        self._processor.stop()

    def is_processing(self) -> bool:
        return self._processor.is_processing()

    @property
    def processor(self) -> CellRulesProcessor:
        return self._processor

    @property
    def config_factory(self) -> CellRulesConfigFactory:
        return self._config_factory

    def _reset_state(self):
        self._current_state_exception = None
        self._current_arg_save_path = ""
        self._current_arg_overwrite = None
        self._current_arg_save_anyway = None

    def _on_started(self, _, workbook: Workbook, worksheet: Worksheet, rules_config: CellRulesConfig):
        self.processing_started.emit(workbook, worksheet, rules_config)

    def _on_finished(self, _, workbook: Workbook, worksheet: Worksheet, rules_config: CellRulesConfig):
        if self._current_state_exception and not self._current_arg_save_anyway:
            self._reset_state()
            self.processing_finished.emit(workbook, worksheet, rules_config)
            return
        exception = None
        try:
            if not self._current_arg_overwrite and os.path.isfile(self._current_arg_save_path):
                raise FileExistsError(f"file '{self._current_arg_save_path}' exists but overwrite is not allowed")
            workbook.save(filename=self._current_arg_save_path)
        except BaseException as e:
            exception = e
        finally:
            self._reset_state()
            self.processing_finished.emit(workbook, worksheet, rules_config, exception)

    def _on_processing_errored(self, _, workbook: Workbook, worksheet: Worksheet, rules_config: CellRulesConfig,
                               error: BaseException):
        self.processing_errored.emit(workbook, worksheet, rules_config, error)

    def _on_failed(self, _, context: FunctionContext, rule: CellRule | PrimitiveDataType, error: BaseException):
        self.rule_execution_failed.emit(context, rule, error)

    def _on_succeed(self, _, context: FunctionContext, rule: CellRule | PrimitiveDataType, result: Any):
        self.rule_execution_succeeded.emit(context, rule, result)

    def _before_executed(self, _, context: FunctionContext,
                         rule_scope_target: CellRule | PrimitiveDataType | List[CellRule]):
        self.before_rule_executed.emit(context, rule_scope_target)
