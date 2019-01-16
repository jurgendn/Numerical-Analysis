# Phương pháp chia đôi - Bisection 
Phương pháp chia đôi dùng để giải phương trình

    * f(x) = 0

*Ngôn ngữ: Python 3*

### **Thư viện sử dụng**
Chương trình sử dụng thư viện **Sympy** đối với tính toán các biến symbolic, đồng thời cũng tạo thuận lợi cho việc sử dụng các hàm tính toán có sẵn.

Để import thư viện **Sympy**, ta sử dụng cú pháp sau:

    > import sympy as sy
    "sy ở đây chỉ là thay thế cho sympy. Thay vì viết sympy thì ta chỉ cần viết sy"
### **Cách chạy chương trình**
Đầu tiên, ta cần phải *import* các thư viện cần thiết:

    > import sympy as sy

Tiếp đó, ta cần nhập vào một số thông tin cần thiết cho phương trình

Chạy file **Bisection.py** bằng cú pháp

    > "Directory Path"\python Bisection.py

B3: Nhập các dữ liệu đầu vào như bậc của đa thức nghiệm và các giá trị khởi đầu:

    "Nhập vào a là một cận của khoảng phân li nghiệm"
    > a =  
    "Nhập vào b là cận còn lại của khoảng phân li nghiệm"
    > b = 
    "Nhập sai số"
    > epsilon = 

Kết quả hiện ra trên màn hình terminal gồm 2 giá trị, gồm nghiệm của phương trình và số vòng lặp

### **Chạy thử ví dụ**
Lấy một bài tập nào đó có 1 nghiệm đúng bằng 1:

    > f(x) = x**3 + sin(x-1) - 1 = 0

Tại dòng 8, chương trình sẽ được config thành:

    > func = x**3 + sy.sin(x-1) - 1

Chạy chương trình với cú pháp 

    > "Directory Path"\python Bisection.py

Giả sử, khoảng phân li nghiệm là [0, 1.5] và cần giải với sai số cỡ 0.000001: 

    > a = 0
    > b = 1.5
    > epsilon = 0.000001

Output của chương trình sẽ là:

    > (0.9999995231628418, 21)

Trong đó thì **0.9999995231628418** là nghiệm và chương trình cần **21** vòng lặp để hoàn thành

Nhận xét rằng **0.9999995231628418** là *kHá ChUẩN* so với nghiệm đúng

* [Trang chính](https://github.com/Billrizer/Numerical-Analysis_Integrated-Equation/tree/Integral-Equation)
