from typing import Any, Sequence

from faker import Faker

from excelfiller.function import ContextFreeFunction

DEFAULT_LOCALE = "zh_CN"


class FakerFunctions(ContextFreeFunction):
    def __init__(self, locale: str | Sequence[str] | dict[str, int | float] = DEFAULT_LOCALE, *args, **kwargs):
        self._locale = locale
        self._faker = Faker(self._locale, *args, **kwargs)

    def on_invoke(self, fake_function: str, locale=None, *args, **kwargs) -> Any:
        if not locale or locale == self._locale:
            cur_faker = self._faker
        else:
            cur_faker = Faker(locale)
        fake_fn = self._get_fake_fn(cur_faker, fake_function)
        if not fake_fn:
            raise ValueError(f"fake function '{fake_function}' not found")
        return fake_fn(*args, **kwargs)

    # noinspection PyMethodMayBeStatic
    def _get_fake_fn(self, faker_instance: Faker, fake_function: str) -> Any:
        return getattr(faker_instance, fake_function, None)
