import numpy as np
import NewtonInterpolation as ni


X = [1, 2, 3, 4, 5, 6, 7, 8]
Y = [1, 4, 9, 16, 25, 36, 49, 64]


# Calc elements:
def calc_Element(X, k, x):
    result = 1
    for i in range(k):
        result = result * (x - X[i])
    return result


# Newton Interpolate calculate
def calc_Newton(X, coef, x):
    n = len(X)
    result = 0
    for i in range(1, n):
        result += coef[i]*calc_Element(X, i, x)
    return result
