import sympy as s
from sympy.abc import x, y, t

# Nhập số lần lặp ở đây
k = int(input("Nhap so lan lap: "))

# Giá trị khởi đầu của y0
y0 = 1
y = y0

for i in range(k):
    # Hàm f(x, y) được nhập trực tiếp ở đây
    f = y0 + s.integrate(-y, (x, 0, x))
    y = f

# In ra đáp án
print(y)
