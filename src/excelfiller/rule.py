import dataclasses
from abc import ABC
from dataclasses import field
from typing import List, Dict, OrderedDict

from simpleconf import BaseTomlConfig, BaseJsonConfig, BaseYamlConfig, MarshmallowSerializable

from excelfiller.common import BasicDataType, filetype_from_suffix, PrimitiveDataType

MAX_ROW = -1
MIN_ROW = -2


@dataclasses.dataclass
class CellRule(object):
    fn: str
    args: List[BasicDataType] = field(default_factory=list)
    kwargs: dict[str, BasicDataType] = field(default_factory=dict)
    per_cell: bool = True


@dataclasses.dataclass
class CellRulesConfig(MarshmallowSerializable, ABC):
    version: int | str = 1
    rules_globals: Dict[str, BasicDataType] = field(default_factory=dict)
    # scope -> list of cell rules or one cell rule or one primitive value for this scope
    rules: Dict[str, List[CellRule] | PrimitiveDataType | CellRule] = field(default_factory=OrderedDict)

    @classmethod
    def create(cls, *args, **kwargs):
        return cls(*args, **kwargs)


@dataclasses.dataclass
class TomlCellRulesConfig(CellRulesConfig, BaseTomlConfig):
    pass


@dataclasses.dataclass
class JsonCellRulesConfig(CellRulesConfig, BaseJsonConfig):
    pass


@dataclasses.dataclass
class YamlCellRulesConfig(CellRulesConfig, BaseYamlConfig):

    def save(self, filepath: str, encoding: str = "utf-8", allow_unicode: bool = True, *args, **kwargs):
        super().save(filepath, encoding, allow_unicode=True,*args, **kwargs)


class CellRulesConfigFactory(object):
    def __init__(self):
        self._config_types = {}

        self._register_defaults()

    @classmethod
    def get_filetype(cls, path: str) -> str:
        ext = filetype_from_suffix(path, with_dot=False)
        if not ext:
            raise ValueError(f"filetype cannot be determined from path '{path}'")
        return ext

    def register(self, filetype: str, config_type: type[CellRulesConfig]):
        if filetype in self._config_types:
            raise ValueError(f"filetype '{filetype}' is already registered")
        self._config_types[filetype] = config_type

    def get(self, filetype: str) -> type[CellRulesConfig] | None:
        return self._config_types.get(filetype, None)

    def is_registered(self, filetype: str) -> bool:
        return self._config_types.get(filetype) is not None

    def unregister(self, filetype: str):
        if self.is_registered(filetype):
            del self._config_types[filetype]

    def unregister_all(self):
        self._config_types.clear()

    def registered_filetypes(self) -> List[str]:
        return list(self._config_types.keys())

    def _register_defaults(self):
        self.register(self.get_filetype("dummy.toml"), TomlCellRulesConfig)
        self.register(self.get_filetype("dummy.json"), JsonCellRulesConfig)
        self.register(self.get_filetype("dummy.yaml"), YamlCellRulesConfig)

    def load(self, path: str, encoding: str = "utf-8", *args, **kwargs) -> CellRulesConfig:
        config_type = self.get(self.get_filetype(path))
        if config_type is None:
            raise ValueError(f"filetype '{self.get_filetype(path)}' is not registered")
        return config_type.load(path, encoding, *args, **kwargs)

    def create(self, filetype: str, *args, **kwargs) -> CellRulesConfig:
        config_type = self.get(filetype)
        if config_type is None:
            raise ValueError(f"filetype '{filetype}' is not registered")
        return config_type.create(*args, **kwargs)