import operator
from functools import reduce
from itertools import product, starmap
from typing import Iterable

import sympy as sy


class LagrangeInterpolation:

    def __init__(self) -> None:
        pass

    def fit(self, observations: Iterable, references: Iterable):
        assert len(observations) == len(references)

        x_var = sy.Symbol('x')

        res = 0
        for idx, (obs, ref) in enumerate(zip(observations, references)):
            _rest = list(observations[:idx]) + list(observations[idx + 1:])

            __denom_coef = list(product([obs], _rest))
            __denom = list(
                starmap(lambda *s: sy.Rational(s[0] - s[1]), __denom_coef))
            __denom = reduce(operator.mul, __denom)

            __nom_coef = list(product([x_var], _rest))
            __nom = list(starmap(lambda *s: s[0] - s[1], __nom_coef))
            __nom = reduce(operator.mul, __nom)
            coef = ref / __denom
            res += __nom * coef
        self.res = res
        return res

    def eval(self, val):
        return self.res.subs({'x': val})
