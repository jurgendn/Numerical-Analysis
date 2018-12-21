import sympy as s
from sympy.abc import x, y, t

# Nhập số lần lặp ở đây
k = int(input("Nhap so lan lap: "))

# Giá trị khởi đầu của y0
y = 0

for i in range(k):
    # Hàm f(x, y) được nhập trực tiếp ở đây
    f = s.integrate(x*x+y*y, (x, 2, x))
    y = f

# In ra đáp án
print(y)
