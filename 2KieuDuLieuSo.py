'''
1-Số Nguyên trong python
2-Số thực trong python:
    Lưu ý : Chúng ta thường viết số thực , phần nguyên và phần thập phân được tách nhau bởi dấy (,) nhưng trogn python
        thì phần nguyên và phần thập phân được cách nhau bởi dấu(.)
    Số thực trong python có độ chính xác mặc định là 15 chữ số thập phân
    Muốn có kết quả chính xác cao hơn chúng ta nên sử dụng hàm Decimal
'''

# Lấy toàn bộ nội dung của thư viện Decimal
from decimal import *
#Lấy tối đa 30 chữ số phần nguyên và phần thập phân 
getcontext().prec = 30
print(Decimal(10/3))
print('\n')
print(Decimal(10)/3)
print('\n')
print(Decimal(10)/Decimal(3))
print(type(10/3),'\n')

# 3-Kiểu phân số : Với hàm Fraction(TS,MS)
from fractions import *     # Lấy toàn bộ nội dung trong thu viện fractions
a=Fraction(6,9)
print(a,'\n')
print(type(a),'\n')

''' 4-Kiểu dữ liệu số phức :
        Gồm 2 thành phần : <Phần thực> + <Phần ảo> j
        Tạo 1 số phức với hàm : complex(<Phần thực>,<Phần ảo>)
'''
#   Gán giá trị của số phức cho 1 biến
coml = 2+10j
print(coml,'\n')
#   Xuất ra phần thực của số phức
print(coml.real,'\n')
#   Xuất ra phần ảo của số phức
print(coml.imag,'\n')

'''5- Các toán tử cơ bản trong python
'''
x=10
y=3
#   Phép chia lấy phần nguyên 
print(x//y , '\n')
#   Lũy thừa mũ Y cơ số X
print(x**y,'\n')

