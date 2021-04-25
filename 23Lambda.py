'''
     Ngoài def đẻ khai báo function object ra thì còn có Lambda 
     Def tạo ra 1 hàm với 1 cái tên xác định còn Lambda trả về 1 hàm 
     Nta ta gọi Lambda là hàm nặc danh(anonymous)
'''

#  I - Gioi thiệu về lambda
'''     Cú pháp : lambda argument1, argument2 ,...: expression
    1- Lambda là 1 expression , ko phải là 1 câu lệnh . Do vậy lambda có thể đặt ở nhiều chỗ mà def ko thể 
    2- Lambda là 1 expression duy nhất ,ko phải là 1 khối lệnh 

'''
# Dùng với từ khóa def
def ave(a,b,c):
    return (a+b+c)/3
print(ave(1,2,3))

# Sử dụng lambda

ave1=lambda a,b,c : (a+b+c)/3
print(ave1(4,5,6))

# Lambda cũng phân biệt biến local và global
def test():
    man=lambda x:x +' is my wife '
    return man          # Trả về 1 hàm nặc danh
a=test()            # Lấy biến a giữ hàm nặc danh
print(a('QANH'))       # Gia trị chuỗi được đưa vào biến x
print(a('Minh'))

# 1 list với các phần tử là hàm lambda
n_lst=[lambda x:x**2 , lambda x:x**3, lambda x:x**4]

n_lst[0](2)    # Truyền giá trị 2 vào x
n_lst[1](3)
n_lst[2](2)

for i in n_lst:
    print(i(3))

# Sử dụng lambda vói dictionary
dict1={'Google':lambda : 'is best',
        'Youtube':lambda :'GOOD'
      }
for i in dict1:
    print(*i)

#       II - Câu điều kiện cho lambda
''' Ta thấy lambda chỉ nhận 1 expression , do đó bạn ko thể chàn câu lệnh điều kiện như bình thường được mà phải 
theo 1 cách khác 
    c1: b if a else c
    c2: (a and b) or c
'''
# kiểm tra xem số x của có ước là 2 và 3 k ?
check1= lambda x:(1 if x%2==0 else 0) if x%3==0 else 0
print(check1(6))
print(check1(4))

#       III- Lambda chồng lambda
