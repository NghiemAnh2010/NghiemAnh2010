# I - Khai báo biến ở trong hàm
v1='Hello'
def f1():
    print(v1,'QANH')
f1() 

''' Biến khai báo ở hàm cha thì có thể sử dụng ở cả hàm cha và hàm con , biến khai báo ở hàm con 
        ko thể sử dụng được hàm cha 
    Một biến local chỉ có giá trị sử dụng trong hàm mà nó được khai báo , nếu ra khỏi hàm đó thì biến đó ko còn 
        tồn tại
'''

# II- Thay đổi gia trị arguments gián tiếp qua parameter 
'''     Ta đã biết 2 thuật ngữ : pass by reference (Truyền tham chiếu ) , pass by value(Truyền tham trị)
'''
num=69
st='How kteam'
lst=[1,2,3,4]
tup=tuple('Education')
def f2(parameter1):
    parameter1='Hello'
    print(parameter1)
f2(num)
f2(st)
f2(lst)
f2(tup)
print('='*15)
print('{}\n{}\n{}\n{}\n'.format(num,st,lst,tup))
# => Ta thấy rằng các biến trên ko thay đổi khi đi qua hàm f2 vì 

def f3(parameter2):
    parameter2[1]='New entry'
print(lst)
f3(lst)
print(lst)
# => Ta thấy rằng lst đã bị thay đổi giá trị vì ta truyền vào và thay đổi giá trị ở địa chỉ của phần tử đó

# III- Sử dụng biến Globals
'''         Cú pháp : global<variable>
'''
def change():
    # Khai báo và khởi tạo giá trị cho biến x
    global x 
    x=20
    print('Hello')
# Gọi hàm change từ đây biến toàn cục x đã được khai báo 
change()
# Tại đây biến x đã đượ định nghĩa và sử dụng trong toàn chương trình 
print(x)    

# IV - Gioi Thiệu hàm Locals và Globals
'''     Hàm locals cho ta biết được những biến local nằm trong chương trình của chúng ta,
        Hàm globals cho ta biết được những biến global nằm trong chương trình 
'''
