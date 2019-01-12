import Taylor_Expansion as te
import sympy as sy
import sympy.functions as syf


# Input Equation:
"y''+p(x)*y'+q(x)*y = f(x)"

# Import x as a symbolic variable
x = sy.Symbol("x")

# Input
n = int(input("Nhap cap khai trien: "))
a = float(input("y(0): "))
b = float(input("y'(0): "))



# Define function and Taylor expansion
p = te.taylor(-x, n)
q = te.taylor(1 + 0*x , n)
f = te.taylor(1-sy.cos(x), n)


# Solve differential equation
def power_series(p, q, f, a, b):
    n = len(p)
    C = [a, b]
    for i in range(2, n):
        result_p = 0
        result_q = 0
        for k in range(1, i):
            result_p += k*C[k]*p[i-k-1]
        for k in range(0, i-1):
            result_q += C[k]*q[i-k-2]
        C.append(((f[i-2]-result_p-result_q))/(i*(i-1)))    
    return C


print(power_series(p, q, f, a, b))
