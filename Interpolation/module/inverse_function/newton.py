from typing import Iterable

import numpy as np
import sympy as sy


class NewtonInterpolation:

    def __init__(self):
        pass

    def __get_divided_differential__(self, X: Iterable, Y: Iterable):
        num_obs = len(X)
        res = np.zeros(shape=(num_obs, num_obs))

        res[:, 0] = Y
        for id_y in range(1, num_obs):
            for id_x in range(0, num_obs - id_y):
                differential = res[id_x + 1][id_y - 1] - res[id_x][id_y - 1]
                divided = X[id_x + id_y] - X[id_x]
                res[id_x][id_y] = differential / divided
        return res

    def fit(self, X: Iterable, Y: Iterable, method: str = 'forward'):
        assert len(X) == len(Y)

        x_var = sy.Symbol('x')

        divided_differential = self.__get_divided_differential__(X=X, Y=Y)

        res = 0
        term_list = []
        term = 1

        if method == 'forward':
            r = divided_differential[0]
        elif method == 'backward':
            r = np.fliplr(divided_differential).diagonal()

        for _, (obs, coef) in enumerate(zip(X, r)):
            res += coef * term
            term_list.append(coef * term)
            term *= (x_var - obs)
        self.res = res
        self.term_list = term_list
        return res

    def add_points(self, X: Iterable, Y: Iterable):
        pass

    def eval(self, val):
        return self.res.subs({'x': val})
