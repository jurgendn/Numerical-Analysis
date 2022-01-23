from functools import reduce
from operator import mul
from typing import Dict, Iterable, Tuple

import numpy as np

from module import LagrangeInterpolation, NewtonInterpolation


class InverseInterpolation:

    def __init__(self, config: Dict) -> None:
        self.method = config['method']
        self.config = config[self.method]
        if config.get('method', False) == 'inverse_function':
            if config['inverse_function']['type'] == 'lagrange':
                self.interpolator = LagrangeInterpolation()
            elif config['inverse_function']['type'] == 'newton':
                self.interpolator = NewtonInterpolation()
        elif config.get('method', False) == 'iterative':
            self.interpolator = NewtonInterpolation()

    def __get_monotonic_sequences__(self, Y: Iterable):
        """Xác định các chuỗi đơn điệu

        Args:
            Y (Iterable): Y

        Returns:
            [List[Tuple]]: Các khoảng đơn điệu, gồm điểm đầu và điểm cuối
        """
        indices = [0]
        diff = np.diff(Y)
        for idx in range(1, len(diff)):
            if diff[idx - 1] * diff[idx] < 0:
                indices.append(idx)
        indices.append(len(diff))
        return list(zip(indices, indices[1:]))

    def __get_isolation_interval__(self, Y: Iterable, target: float):
        """Tìm khoảng phân ly nghiệm

        Args:
            Y (Iterable): Y
            target (float): Giá trị cần tính

        Returns:
            [List[Tuple]]: Tập các khoảng phân ly nghiệm
        """
        indices = []
        diff = list(map(lambda ref: target - ref, Y))
        for index in range(1, len(Y)):
            if diff[index - 1] * diff[index] < 0:
                indices.append((index - 1, index))
        return indices

    def __get_divided_differential__(self, X: Iterable, Y: Iterable):
        """Bảng tỉ hiệu
        """
        num_obs = len(X)
        res = np.zeros(shape=(num_obs, num_obs))

        res[:, 0] = Y
        for id_y in range(1, num_obs):
            for id_x in range(0, num_obs - id_y):
                differential = res[id_x + 1][id_y - 1] - res[id_x][id_y - 1]
                divided = X[id_x + id_y] - X[id_x]
                res[id_x][id_y] = differential / divided
        return res

    def __get_containing_monotonic_seq__(self, monotonic_seq: Iterable,
                                         isolation_interval: Iterable):
        """Xác định khoảng đơn điệu chứa khoảng phân ly nghiệm

        Args:
            monotonic_seq (Iterable): Các khoảng đơn điệu
            isolation_interval (Iterable): Các khoảng phân ly nghiệm

        Returns:
            [Dict]: {Khoảng phân ly: Khoảng chứa}
        """
        res = {}
        for interval in isolation_interval:
            out = list(
                filter(
                    lambda s: (interval[0] - s[0]) * (interval[1] - s[1]) <= 0,
                    monotonic_seq))[0]
            res[interval] = out
        return res

    def __forward_or_backward__(self, isolation_interval: Tuple,
                                containing_monotonic_sequence: Tuple):
        """Newton tiến or lùi?

        Args:
            isolation_interval (Tuple): Các khoảng phân ly nghiệm
            containing_monotonic_sequence (Tuple): Khoảng đơn điệu

        Returns:
            [str]: tiến/lùi
        """
        if containing_monotonic_sequence[1] - isolation_interval[
                0] > isolation_interval[1] - containing_monotonic_sequence[0]:
            return 'forward'
        return 'backward'

    def __fit_inverse_function__(self, X: Iterable, Y: Iterable, target: float):
        """Phương pháp dùng hàm ngược

        Args:
            X (Iterable): X
            Y (Iterable): Y
            target (float): Giá trị cần tính ngược

        Returns:
            (List): Tập nghiệm
        """
        monotonic_seq = self.__get_monotonic_sequences__(Y=Y)
        isolation_interval = self.__get_isolation_interval__(Y=Y, target=target)
        containing_seq = self.__get_containing_monotonic_seq__(
            monotonic_seq=monotonic_seq, isolation_interval=isolation_interval)

        res = []
        for seq in containing_seq.values():
            self.interpolator.fit(X=Y[seq[0]:seq[1] + 1],
                                  Y=X[seq[0]:seq[1] + 1])
            res.append(self.interpolator.eval(target))
        self.res = res
        return res

    def __fit_iterative__(self, X: Iterable, Y: Iterable, target: float):
        """Phương pháp lặp

        Args:
            X (Iterable): X
            Y (Iterable): Y
            target (float): Giá trị cần tính

        Returns:
            [List]: Tập nghiệm
        """
        h = X[1] - X[0]

        def generate_factorial(index: int):
            return reduce(mul, range(1, index + 1))

        def generate_coef(val, index: int):
            base_list = range(0, index + 1)
            terms = map(lambda term: val - term, base_list)
            return reduce(mul, terms) / generate_factorial(index)

        def get_function(Y: Iterable, val: float):
            max_order = len(Y) - 1
            res = val
            for order in range(1, max_order + 1):
                coef = generate_coef(val, order)
                res -= np.diff(Y, order)[0] * coef
            res = res + generate_coef(val, 1) * np.diff(Y, 1)[0]
            return res

        monotonic_seq = self.__get_monotonic_sequences__(Y=Y)
        isolation_interval = self.__get_isolation_interval__(Y=Y, target=target)
        containing_seq = self.__get_containing_monotonic_seq__(
            monotonic_seq=monotonic_seq, isolation_interval=isolation_interval)
        """Note nhẹ
        """
        output = []
        for case in containing_seq.items():
            interval = case[0]
            seq = case[1]
            method = self.__forward_or_backward__(
                isolation_interval=interval, containing_monotonic_sequence=seq)

            if method == 'forward':
                x = X[interval[0]:]
                y = Y[interval[0]:]
                u = (target - y[0]) / h
                self.interpolator.fit(X=x, Y=y, method=method)
                # term_list = self.interpolator.term_list
                # phi_u = sum(term_list) - term_list[1]
                # phi_u = target - y[0] - phi_u/h
                for ite in range(self.config['max_ite']):
                    u_old = u
                    u = get_function(y, u)
                    tol = np.abs(u - u_old)
                    if tol < float(self.config['tolerance']):
                        break
                x = x[0] + u*h
                output.append({
                    'root': x,
                    'iteration': ite + 1,
                    'tol': tol,
                    'isConvergence': bool(tol < 1e-4)
                })

            elif method == 'backward':
                x = X[:interval[1] + 1]
                y = Y[:interval[1] + 1]
                u = (target - y[-1]) / h
                # self.interpolator.fit(X=x, Y=y, method=method)
                # term_list = self.interpolator.term_list
                # phi_u = sum(term_list) - term_list[1]
                # phi_u = target - y[-1] - phi_u/h

                for ite in range(self.config['max_ite']):
                    u_old = u
                    u = get_function(y, u)
                    tol = np.abs(u - u_old)
                    if tol < float(self.config['tolerance']):
                        break
                x = x[-1] + u*h
                output.append({
                    'root': u,
                    'iteration': ite + 1,
                    'tol': tol,
                    'isConvergence': bool(tol < 1e-4)
                })

        return output

    def fit(self, X: Iterable, Y: Iterable, target: float):
        assert len(X) == len(Y)
        if self.method == 'inverse_function':
            res = self.__fit_inverse_function__(X, Y, target)
        elif self.method == 'iterative':
            res = self.__fit_iterative__(X, Y, target)
        return res
