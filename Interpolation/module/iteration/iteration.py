from typing import Iterable, Tuple

import numpy as np
from sympy.core.numbers import Float


class IterativeApproximation:
    """Iterative Approximation Method
    Chỉ dùng với nội suy mốc cách đều
    """

    def __init__(self) -> None:
        pass

    def __get_monotonic_sequences__(self, references: Iterable):
        indices = [0]
        diff = np.diff(references)
        for idx in range(1, len(diff)):
            if diff[idx - 1] * diff[idx] < 0:
                indices.append(idx)
        indices.append(len(diff))
        return list(zip(indices, indices[1:]))

    def __get_isolation_interval__(self, references: Iterable, target: Float):
        indices = []
        diff = list(map(lambda ref: target - ref, references))
        for index in range(1, len(references)):
            if diff[index - 1] * diff[index] < 0:
                indices.append((index - 1, index))
        return indices

    def __get_divided_differential__(self, observations: Iterable,
                                     references: Iterable):
        num_obs = len(observations)
        res = np.zeros(shape=(num_obs, num_obs))

        res[:, 0] = references
        for id_y in range(1, num_obs):
            for id_x in range(0, num_obs - id_y):
                differential = res[id_x + 1][id_y - 1] - res[id_x][id_y - 1]
                divided = observations[id_x + id_y] - observations[id_x]
                res[id_x][id_y] = differential / divided
        return res

    def __forward_or_backward__(self, isolation_interval: Tuple,
                                monotonic_sequence: Tuple):
        if monotonic_sequence[1] - isolation_interval[0] > isolation_interval[
                1] - monotonic_sequence[0]:
            return 'forward'
        return 'backward'

    def fit(self, observations: Iterable, references: Iterable):
        assert len(observations) == len(references)

        divided_differential = self.__get_divided_differential__(
            observations=observations, references=references)

        res = 0
        # Statements here
        self.res = res
        return res

    def eval(self, val):
        return self.res.subs({'x': val})
