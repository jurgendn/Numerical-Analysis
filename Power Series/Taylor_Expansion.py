import sympy as sy
import numpy as np
import sympy.functions as spf
import matplotlib.pyplot as plt


# Define the variable and the function to approximate
x = sy.Symbol('x')


# Factorial function
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)


# Taylor approximation at x0 of the function 'function'
def taylor(function, n):
    i = 0
    p = []
    while i <= n+1:
        tmp = (function.diff(x, i).subs(x, 0))/(factorial(i))*(x-0)**i
        tmp2 = sy.lambdify(x, tmp)
        p.append(tmp2(1))
        i += 1
    return p
