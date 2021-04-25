
# I - Gioi Thiệu Về Return
'''         Cú pháp: return [object]
    + Object ở đây là 1 đối tượng bất kì của 1 lớp nào đó , có thể là số (number), chuỗi (string),list,tuple ,
        hàm (sẽ biết rõ hơn khi tìm hiểu decorator), lớp class , thậm trí ta có thể bỏ trống object, lúc này 
        return sẽ trả về giá trị None
    + Khi return được gọi , hàm được kết thúc và trả về kết quả ra ngoài hàm .Kết quả được đưa cho 1 biến nào đó 
        hứng 
'''
def func(width,height):
    s=width*height
    return s
width = 10
height=20
showI=func(width,height)
print(showI)

# Return còn được sử dụng để ngắt hàm , mọi câu lệnh đằng sau return sẽ được bỏ qua 

# II-   Dùng return để trả về nhiều giá trị 1 lúc
'''         Với thiết kế đặc biệt của Python bạn có thể unpack các object trả về 
'''

# Ví dụ ta có thể khai báo các biến như sau
a,b,c='anh',1,2
n,b,q=('N','A',20)
print(a)
print(n,b,q)

# Hàm trả về nhiều giá trị
def returns(width,height):
    s=width*height
    p=width+height
    return s,p
result=returns(5,10)
print(result)

# Bài tập :
''' Hàm f(x)= x^3 +2x^2-4*x+1
'''
def f_x(x):
    return  x**3 +2*x**2-4*x+1

lst1= [(-5,-20), (-4,-15), (-3,4), (-2,9), (-1,7), (0,1),(1,-7),(2,-9),(4,81),(5,130)]
A1=[]
B1=[]
def check(lst):
    for i in lst:
        result=f_x(i[0])
        if result == i[1]:
            A1.append(i)
        else:
            B1.append(i)
    return A1,B1
A,B=check(lst1)
def sum1(lst):
    s=0
    for value in lst:
        s+=value[1]
    return s
print('Ket qua can tim la:')
print(abs(sum1(A)-sum1(B)))