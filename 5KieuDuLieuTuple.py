'''                               Tuple
Tuple là 1 container sử dụng nhất nhiều trong python
Tuple gồm các yếu tố sau :
    1-Được giới hạn bởi dấu () , tất cả những gì nằm trong nó là những phần tử của tuple
    2-Các phần tử của Tuple được phân cách nhau ra bởi dấu phẩy (,).
    3-Tuple có khả năng chứa mọi giá trị, đối tượng trong Python.
    4-Tốc truy nhập của tuple nhanh hơn list
    5-Dung lượng chiếm của bộ nhớ nhỏ hơn list
    6-Bảo vệ dữ liệu của bạn sẽ không bị thay đổi
    7- Có thể dùn làm key của dictionary
Khởi tạo tuple :
    (<giá trị thứ nhất>, <giá trị thứ hai>, .., <giá trị thứ n – 1>, <giá trị thứ n>)
'''

t1=(1,2,3,4)        # Khởi tạo 1 tuple 
print(t1,'\n')
print(type(t1),'\n')

# Ở đây ta thấy rằng t2 không còn là 1 tuple mà t2 bây giờ thuộc lớp int
t2=(10)
print(t2,'\n')
print(type(t2),'\n')
# Vì khi bạn viết 1 gtri nào đó đặt trong dấu () thì nó được xem là 1 giá trị và khi tính toán dấu () thường được ưu tiên

# Muốn khởi tạo 1 tuple có 1 phần tử ta phải thêm dấu , sau chúng
t3=(2,)
print(t3,'\n')
print(type(t3),'\n')

# 1-Sử dụng Contructor tuple 
'''         Cú pháp : tuple(iterable)
            Giongos với contructor list ,khác là contructor tuple sẽ tạo ra 1 tuple
'''
t4=tuple('quanganh')        # Với iterable là 1 chuỗi
t5=tuple([1,2,3,4,5])       # Với iterable là 1 list
print(t4,'\n')
print(t5,'\n')

# Tuple không cho phép bạn sử dụng trực tiếp comprehension như sau
t6=(i for i in range(10) if i%2==0 )
# MÀ PHẢI THÔNG QUA tuple
print(tuple(t6),'\n')

'''         II Một số toán tử với tuple 
    Toán tử của tuple cũng giống với toán tử của chuỗi 
'''
# 1-Toán từ + :
t7=(1,2,3,4)
t7 += (5,6,7)
print(t7,'\n')

# 2- Toán tử * :
t8=('a','b',1,2,3)
t9=t8*2
print(t9,'\n')

# 3-Toán tử in :  
t10=(1,2,3)
print('a' in t9,'\n')
print(t10 in t8 ,'\n')

# 4-Indexing và cắt tuple : Hoàn toàn giống với indexing và cắt list 
print(t9,'\n')

print(t9[0],'\n')   # => a
print(t9[-1],'\n')  # => 3
print(t9[0:4],'\n')     # => ('a', 'b', 1, 2)

print(t9[::2],'\n')     # => ('a' , 1,3,'b',2)

# 5- Thay đổi nội dung của tuple 
'''     Tuple và chuỗi đều là 1 dạng hash object nên việc ta thay đổi nội dung bên trong chúng 1 cách trực tiếp 
trên lý thuyết là ko
'''

# 6- Ma Trận : Tương tự như ma trận bên list

t11=((1,2,3),(4,5,6))   # 1 ma trận 2 chiều
print(t11,'\n')

t12=((20,10,2001),)     # ma trận 1 chiều

t13=((1,2,3),[4,5])
print(t13,'\n')
print(t13[1][1],'\n')   # =>5

# 7- Tuple có phải luôn luôn là 1 dạng hash object không ?
'''     Hash object là 1 đối tượng bạn không thể thay đổi nội dung bên trong nó và phần thay đổi nội dung trong 
    tuple bạn cx ko thể thay đổi nội dung cho nó
        Nhưng nếu bên trong tuple là 1 list Và list là 1 dạng unhash object ==> ta có thể thay đổi nội dung của nó

'''

t14=([1,2,3,4,5],)
t14[0][1]='a'               # Thay giá trị ở vị trí [0][1]
print(t14,'\n')

 #  => Một tuple được coi là 1 hash object nếu nó chưa các phần tử bên trong nó đều là các hash object

'''          
                         III-CÁC PHƯƠNG THỨC CỦA TUPLE
'''
 # 1-Phương thức count() :
'''        Cú pháp : <Tuple>.count(value)
            Trả về số nguyên chính là số lần xuất hiện của value trong tuple
'''
t15=(1,2,3,6,2,7,2)
a=t15.count(2)
print(a,'\n')

# 2-Phương thức index():
'''         Cú pháp : <Tuple>.index(sub[, start[, end]])
            Trả về 1 số nguyên là vị trí đầu tiền sub khi dò từ trái sang phải trong tuple 
            Nếu sub không có trong chuỗi thì sẽ có lỗi 
'''

b=t15.index(2)
print(b,'\n')
