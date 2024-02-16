import random
from typing import Dict, Callable, Any

from excelfiller.function import ContextFreeFunction


class RandomFunctions(ContextFreeFunction):

    def __init__(self, seed=None):
        self._random = random.Random(seed)
        self.functions: Dict[str, Callable] = {
            "randint": self._random.randint,
            "random": self._random.random,
            "uniform": self._random.uniform,
            "choice": self._random.choice,
            "randrange": self._random.randrange,
            "getrandbits": self._random.getrandbits,
            "gauss": self._random.gauss,
            "triangular": self._random.triangular,
            "expovariate": self._random.expovariate,
            "vonmisesvariate": self._random.vonmisesvariate,
            "gammavariate": self._random.gammavariate,
            "betavariate": self._random.betavariate,
            "paretovariate": self._random.paretovariate,
            "weibullvariate": self._random.weibullvariate,
            "lognormvariate": self._random.lognormvariate,
            "normalvariate": self._random.normalvariate
        }

    def on_invoke(self, random_function: str, *args, **kwargs) -> Any:
        rand_fn = self.functions.get(random_function, None)
        if rand_fn is None:
            raise ValueError(f"function '{random_function}' not found")
        else:
            return rand_fn(*args, **kwargs)
