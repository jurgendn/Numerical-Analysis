# Phương pháp chuỗi lũy thừa
Phương pháp chuỗi lũy thừa được sử dụng để giải các phương trình vi phân có dạng

    * y'' + p(x)y' + q(x) = f(x)

*Ngôn ngữ: Python 3*

### **Thư viện sử dụng**
Chương trình sử dụng thư viện **Sympy** đối với tính toán các biến symbolic, đồng thời cũng tạo thuận lợi cho việc sử dụng các hàm tính toán có sẵn.

Để import thư viện **Sympy**, ta sử dụng cú pháp sau:

    > import sympy as...
### **Các moudule được sử dụng**
Chương trình sử dụng 1 file là "**Taylor_Expansion.py**" để khai triển Taylor cho các hàm p(x), q(x) và f(x) cho bởi phương trình đầu bài viết.

Đầu tiên, ta cần phải *import* các thư viện cần thiết:

    > import Taylor_Expansion  as te
    > import sympy as sy
    > import sympy.function as syf
Tiếp đó, ta cần nhập vào một số thông tin cần thiết cho phương trình

Nhập vào bậc của đa thức khai triển Taylor cho cách hàm số:

    > n = int(input("Degree: "))
Sau đó, ta lưu lại các hệ số của khai triển Taylor vào các array p, q, f đã được định nghĩa. 

### **Cách định nghĩa các hàm p, q, f:**

Trong file **Power_Series.py**, ta thấy có đoạn sau:

    > p = te.TaylorExpansion('p is here', n)
    > q = te.TaylorExpansion('q is here', n)
    > f = te.TaylorExpansion('f is here', n)

Giả dụ ta cần giải phương trình

    > y'' - x.y' + y = 1 - cos(x)
Khi đó, p, q, f sẽ được nhập như sau:

    > p = te.TaylorExpansion(-x, n)
    > q = te.TaylorExpansion(1 + 0*x, n)
    > f = te.TaylorExpansion(1 - sy.cos(x), n)

## Chạy chương trình
B1: Nhập các dữ liệu đầu vào như các hàm p(x), q(x), f(x) như đã hướng dẫn bên trên

B2: Chạy file **Power_Series.py** bằng cú pháp

    > 
