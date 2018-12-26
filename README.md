# Giải tích số - Phương trình vi phân
* Ngôn ngữ: Python 3	
* Chương trình gồm 2 phương pháp: 
	* Phương pháp Picard
	* Phương pháp chuỗi lũy thừa
## Phương pháp Picard
#### Import thư viện **sympy**
	* Để có thể chạy được chương trình, cần phải import thư viện sympy
	* pip install sympy --user
#### Cấu trúc chương trình
##### Chương trình sử dụng biến symbolic. Do đó, kết quả trả về là dạng symbolic, tức là một biểu thức chứa biến. Đầu tiên:
	* from sympy.abc imprort x, y
##### Dòng này dùng để import các biến x, y là các biến symbolic
##### Chúng ta cũng cần lựa chọn số lần lặp thích hợp cho phương pháp, do đó ta có 
	> k = int(input("Nhập số lần lặp: "))
##### Nghĩa là chương trình sẽ được lặp k lần, nghiệm theo thứ tự tìm được là y[0], y[1], y[2],..., y[k-1]. Lúc này quá trình lặp sẽ dừng, nghiệm của phương trình vi phân sẽ là y[k-1]
##### Mọi phương trình vi phân đều cần có một giá trị y(x0). Ta sẽ khai báo y0 tại đây
	* Khai báo y0:
	> y = y0
##### Dưới đó là vòng lặp for:
	> for i in range(k):
		> f = s.integrate("f(x, y)", (x, x0, x))
		> y = f
##### Từng dòng sẽ được giải thích như sau:
	> for i in range(k):
##### Lặp k lần, dễ vlol. Dòng tiếp theo:
	> f = s.integrate("f(x, y)", (x, x0, x))
##### Sau bước này, giá trị trả về cho f là một hàm số của x. Thực ra, đây chính là giá trị của y. Như vậy, ta sẽ cần một bước gán nhỏ:
	> y = f
##### Tiếp tục vòng lặp. Giá trị của y(x) lúc này lại được thay lại vào trong:
	> f = s.integrate("f(x, y)", (x, x0, x))
		> y = f
##### Sau mỗi một lần lặp, giá trị của y(x) trả về càng ngày càng gần với ngiệm đúng của phương trình. Cần lưu ý rằng nghiệm này chỉ đúng trên một miền nhất định, mà cụ thể hơn là miền thỏa mãn điều kiện hàm f(x, y) là hàm lipschitz theo y trên đó. 
##### Cuối cùng, ta in ra kết quả 
	> print(y)
##### Lấy ví dụ là một phương trình trong giáo trình:
	* y' = x**2 + y**2
	* y(0) = 0
##### Tức là, input của chương trình sẽ là:
	> f(x, y) = x**2 + y**2
	> y = 0
	> x0 = 0
##### Mạnh dạn đề xuất 3 lần lặp, theo đó, chương trình sẽ được config lại thành:
	> y = 0
	> for i in range(k):
		* f = s.integrate(x**2 + y**2, (x, 0, x))
		* y = f
##### Cuối cùng, với input như trên, output sẽ là:
	> y(x) = 
