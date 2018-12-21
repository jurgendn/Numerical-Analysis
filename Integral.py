import NewtonInterpolation as ni
import matplotlib.pyplot as plt
import Calculate as cal
import numpy as np
import math as m


# Tinh f(x, y) tai (x, y)
def f(x, y):
    result = -y
    return result


# Xap xi ham
def integral(f, y0, x0, h, k, n):
    x = np.arange(x0, x0 + k * h, h)
    I = [0]*k
    coef = [0]*k
    I[0] = y0
    for i in range(n):
        for j in range(1, k):
            I[j] = I[j - 1] + h*(f(x[j - 1], cal.calc_Newton(x, coef, (x[j-1]+x[j])/2)) + f(
                x[j], cal.calc_Newton(x, coef, (x[j]+x[j-1])/2)))*1/2
        plt.plot(x, I, "-")
        coef = ni.Interpolate(x, I)
    plt.show()
    return coef


print(integral(f, 1, 0, 3, 25, 5))
