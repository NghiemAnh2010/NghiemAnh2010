'''
   1- Định dang chuỗi bằng toán tử % 
        Cú pháp : <Chuỗi> %(gía trị thứ 1, giá trị thứ 2, .... giá trị thứ n)
        Một số toán tử % cơ bản trong python
        1- %s : Gía trị của phương thức _str_ đối với đối tượng đó
        2- %d : Gía trị của 1 số -Nếu là số thực thì sẽ chỉ lấy phần nguyên (chuyển sang hệ số nguyên)
        3- %r : Gía trị của phương thức _repr_ của đối tượng đó 
        4- %<số chữ số thập phân>f : Gía trị của 1 số -Nếu là số sẽ được chuyển sang số thực
        5- %c : Ký tự 
        6- %i : số nguyên thập phân có dấu
        7- %u : số nguyên hệ bát phân ko dấu 
        8- %o : số nguyên hệ thập phân ko dấu  
'''
s='%s Quang %s'
s1 = s%('Hello','Anh')
print(s1,'\n')

d="Quang Anh %d%d" %(20,10.5)
print(d,'\n')

f="QuangAnh %.5f" %(2010)
print(f,'\n')
'''
        Sự khác nhau giữa %s và %r : Mọi đối tượng trong python đều là các đối tượng của 1 lớp nào đó , do đó nó có 
            thuộc tính riêng , phương thức riêng , 2 phuong thức đó là _str_ và _repr_

'''
class SomeThing:
        def __repr__(self):
            return 'Day la __repr__'
        def __str__(self):
            return 'Day la __str__'

#Khai báo 1 đối tượng thuộc lớp SomeThing()
sthing = SomeThing()
print(type(sthing),'\n')
r5='%r' %(sthing)       
s5='%s' %(sthing)
print(r5,'\n')
print(s5,'\n')
'''
    ==> %s thay thế cho giá trị của phương thức __str__ tạo nên đối tượng đó
        %r thay thế cho giá trị của phương thức __repr__ tạo nên đối tượng đó
'''

''' 
    2-Định dạng bằng chuỗi f (f-string)
        Cú pháp : f'giá trị trong chuỗi'
'''

# Đây là 1 chuỗi f-string
f1 = f'quanganh'
name="Quang Anh"
address="Hung Yen"
number_phone="0816615699"
result= f' Name: {name}\n Address: {address}\n NumberPhone: {number_phone}\n'
print(result)

''' Ở đây lại có 1 vấn đề : nếu bạn muốn có 1 chuỗi như này : '1:{one} ,2:{two},3{variable} '
        mà bạn chỉ muốn định dạng mỗi chỗ {variable} thôi thì ta phải thêm {} vào các nơi mà ta không muốn định nghĩa
            cũng giống như cách ta muốn có 1 dấu \ để Python k hiểu nó là 1 Escape Sequence ta phải thêm dấu  \
'''
variable1='threee'
v1 = f'1:{{one}} , 2:{{two}} , 3:{variable1}'
print(v1) 

''' 
    3- Định Dạng Bằng Phương Thức Format (Định dạng cho phép Python đinh dạng 1 chuỗi 1 cách tuyệt vời)
'''

fm='a:{} , b:{}, c:{}'.format(1,2,3)
print(fm,'\n')
# Tương tự như dùng format trên với định dạng bằng toán tử %
fm1='1 : %s, 2 : %s, 3 : %s' %('a','b','c')
print(fm1,'\n')

# Với phương thức này thì giá trị ở vị thứ nhất sẽ được thay thế cho vị trí thứ nhất ở trong chuỗi ...
fm2=' a:{1} , b:{2} , c:{0}' .format(1,2,3)
print(fm2,'\n')
# Phương thức này cũng không quá khắt khe viêc các giá trị số các nơi cần định dạng trong chuỗi
fm3='NBQA {0}'.format(2010,2001)
print(fm3,'\n')

# Nếu việc định dạng bằng các vị trí được đánh số thì bạn co thể đinh dạng rõ rằng như sau
fm4='Name={one} , Age={two}'.format(one = 'Qanh',two=20)
print(fm4,'\n')

''' Định dạng format còn giúp nội dung tăng tính thẩm mĩ cụ thể là phương thức này còn giúp bạn căn lề 
    Căn lề trái : {:(C)<n}
    Căn lề phải : {:(c)>n}
    Căn ở giữa  : {:(c)^n}
    Căn lề trái thì thừa phải
    Căn lề phải thì thừa trái
Với c là kí tự bạn muốn thay thế vào chỗ trống , nếu để trống thì sẽ là kí tự khoảng trắng 
    n là số kí tự dùng để căn lề
'''
fm5='{:<10}'.format('quanga')
fm6='{:>10}'.format('quanga')
fm7='{:^10}'.format('nbqa')
fm8='{:*^10}'.format('quanganh')
print(fm5,'\n')
print(fm6,'\n')
print(fm7,'\n')
print(fm8,'\n')
# Ta có ví dụ sau:
row1='+ {:->5} + {:-^15} + {:-<9} +'.format('','','')
row2='| {:<5} | {:^15} | {:>9} |'.format('ID','Ho va Ten','Noi sinh')
row3='| {:<5} | {:^15} | {:>9} |'.format('123','Yui hanato','Japan')
row4='| {:<5} | {:^15} | {:>9} |'.format('6968','Sunny','USA')
row5='+ {:-<5} + {:-^15} + {:->9} +'.format('','','')
print(row1)
print(row2)
print(row3)
print(row4)
print(row5)