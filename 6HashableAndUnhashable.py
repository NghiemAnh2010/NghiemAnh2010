'''       
    I- Gioi Thiệu Về hàm id()
        Cú pháp: id( <giá trị> )
        Mọi thứ trong python xoay quanh các đối tượng và các giá trị ở đây chính là 1 đối tượng
        Hàm id trả về 1 số nguyên (int hoặc longint)
           + Gía trị là là 1  giá trị duy nhất và là hằng số không thay đổi suốt chương trình.
           + Giá trị trả về của hàm id là địa chỉ của giá trị (đối tượng) đó trong bộ nhớ.
'''

id1=id(7)
print(id1,'\n')

id2=id('qanh')
print(id2,'\n')

id3='qanh'
id4=id(id3)         # id4 là 1 biến , lấy địa chỉ của biến id3 , với 1 đối tg là 1 biến số mỗi lần cho ra 1 vùng nhớ khac nhau
print(id4,'\n')
print(id(id3),'\n')

id5=9
id6=id(id5)
print(id(id5),'\n')
print(id6,'\n')

# 1- Toán tử là 1 phương thức 
n=19
print(n+1,'\n')
print(n.__add__(1),'\n')        # Tương tự n+1

print(n-2,'\n')
print(n.__sub__(2),'\n')

print(n.__radd__(1),'\n')       # Tương tự 1+n
print(n.__sub__(10),'\n')       # Tương tự 10-19
#==> Mỗi tóan tử của mỗi đỗi tượng sẽ có toán tử đi kèm

# 2- Khác biệt về toán tử Hash object và unhash object

# Với hash object:
h1='Nqanh'
h2='qanh'
print(id(h1),'\n')
print(id(h2),'\n')

h1=h1+'anh'
h2+='anh'
print(id(h1),'\n')      # Ta thấy sự thay đổi
print(id(h2),'\n')      # Ta cũng thấy sự thay đổi

# Với unhash
un1=[1,2,3]
un2=[4,5,6]
print(id(un1),'\n')
print(id(un2),'\n')

un1 += [9]          # <==> un1.__add__([9]) : là 1 phương thức
un2 = un2 +[9]

print(id(un1),'\n')         # Ta thấy địa chỉ ở đây giữ nguyên
print(id(un2),'\n')         # ở đây địa chỉ đã bị thay đổi 
'''==> Do khi dùng toán từ = + nghĩa là ta gán giá trị cho biến un2 nên địa chỉ của un2 sẽ bị thay đổi ,  
            còn khi ta dùng += nghĩa là ta đã gián tiếp gọi 1 phương thức
'''
# Các hashable không như unhash vì các hash object ko có các phương thức iadd hay imul như các unhash  

# Tại sao Các hashable không như unhash , các hash object ko có các phương thức iadd hay imul như các unhash
'''     
   Với hash object, bạn không thể thay đổi nội dung của nó. Do đó, Python sẽ xin đủ khoảng
    trống để lưu trữ dữ liệu của bạn, không nhiều hơn và cũng không ít hơn. Giúp không hoang phí bộ nhớ của bạn
    Nên khi bạn cộng thêm thứ gì đó , python k bt nhét nó vào đâu nên nó đành đến 1 địa chỉ với có đủ khoảng trống

   Với unhash thì khác , là 1 đối tượng bạn có thể thay đổi nội dung của nó , do đó python sẽ xin dư vùng nhớ để
    chừa chỗ cho các giá trị tiếp theo bạn có thêm thay đổi
