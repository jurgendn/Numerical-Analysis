from typing import Dict, Iterable

from module import LagrangeInterpolation


class InverseInterpolation:

    def __init__(self, config: Dict) -> None:
        self.method = config['method']
        if self.method == 'lagrange':
            self.interpolator = LagrangeInterpolation()
        elif self.method == 'newton':
            self.interpolator = LagrangeInterpolation()

    def fit(self, observations: Iterable, references: Iterable):
        self.res = self.interpolator.fit(observations=observations,
                                         references=references)
        return self.res

    def eval(self, val):
        return self.interpolator.eval(val)
