'''                             KIỂU DỮ LIỆU SET 
Set là 1 container ,tuy nhiên không được sử dung nhiều như list và tuple
Set gồm các yếu tố :
    + Được giới hạn bởi cặp ngoặc {}, tất cả những gì nằm trong đó là những phần tử của Set.
    +Các phần tử của Set được phân cách nhau ra bởi dấu phẩy (,).
    + Set không chứa nhiều hơn 1 phần tử trùng lặp
Set chỉ có thể chứa các iterable , nhưng chính nó không phải là 1 iterable , vì vậy ta không thể chứa set trong set
'''
# Khởi tạo set
se1={1,2,3,4,5}
se2={2,4,6,1,2,3,5,5,5}         # Các giá trị trừng lặp sẽ bị loại bỏ
print(se1,'\n')
print(se2,'\n')

# Khởi tạo bằng các này thì ít nhất phải có 1 giá trị
se3={}
print(type(se3),'\n')       # se3 không thuộc kiểu set

# 1- Sử dụng Conprehension 
se4={ i for i in range(5)}
print(se4,'\n')

# 2- Sử dụng Contructor set : 
'''     cú pháp : set(iterable)
        Cũng giống như contructor list , khác là set contructor sẽ cho ra 1 set
'''
se5='NghiemAnh'
se6=set(se5)
print(se6,'\n')         # set khong quan tâm đến vị trí của các phần tử 

lst1=[1,2,3,4,5,6,1,2]
se7=set(lst1)
print(se7,'\n')

# Cách tạo ra được 1 empty set
c1=''
se8=set(c1)
print(se8,'\n')
print(type(se8),'\n')

''' I- Một số toán tử với Set 
'''
# 1-Toán tử in :
'''     Cú pháp : valuee in <Set>
        Trả về kqua True nếu value xuất hiện trong <Set> và False nếu ngược lại 
'''
print(2 in se7,'\n')

# 2-Toán tử - :
'''         Cú pháp : <Set1>-<Set2>
            Trả về kqua là 1 set gồm các phần tử  chỉ thuộc set1 mà không thuộc set2
'''
se8={4,5,6,7,8}
se9=se7-se8                 # se9 ={1,2,3}
print(se9,'\n') 

# 3-Toán tử & :
'''         Cú pháp : <Set1> & <Set2>
            Trả về 1 set chứa các phần tử vừa tồn tại trong set1 vừa tồn tại trong set2
'''
se10=se7&se8        # => se10={4,5,6}
print(se10,'\n')

# 4-Toán tử | :
'''         Cú pháp : <Set1> | <Set2>
            Trả về 1 set chứa các phần tử tồn tại trong set1 or set2
'''

# 5-Toán tử ^ :
'''         Cú pháp : <Set1> ^ <Set2>
            Trả về 1 set chứa tất cả các phần tử chỉ tồn tại ở 1 trong 2 set
'''
se11={1,2,3,4,5}
se12={6,7,8,9,10}
se13={2,3,4,5,6,7}
se14=se11^se12
se15=se11^se13
print(se14,'\n')
print(se15,'\n')

# Vì set không quan tâm đến vị trí của các phần tử nên Indexing và cắt Set trong python không được hỗ trợ

'''     II-CÁC PHƯƠNG THỨC CỦA SET
'''
#  1- Phương thức clear :
'''     Cú pháp : <Set>.clear()
        Loại bỏ hết các phần tử có trong set
'''

# 2-Phương thức pop :
'''         Cú pháp : <Set>.pop()
            Trả về 1 giá trị được lấy ra từ set , đồng thời loại bỏ giá trị đó ra khỏi set
            Nếu set rỗng sẽ có lỗi
            Trong 1 sô trường hợp , bạn sẽ pop được các giá trị từ bé đến lớn .Nhưng đó không phải bản chất của pop
'''
set1={2,3,4,5,6,7}
s=set1.pop()
print(s,'\n')
print(set1,'\n')

# 3- Phương thức remove :
'''         Cú pháp :<Set>.remove(value)
            Loại bỏ giá trị value ở trong set , nếu như value không có trong set thì sẽ có thông báo lỗi 
'''
set1.remove(7)
print(set1,'\n')

# 4- Phương thúc discard 
'''         Cú pháp : <Set>.discard(value)
            Loại bỏ giá trị value trong set , nếu value không có trong set thì bỏ qua
'''
set2={1,2,3,4,5,6}
set2.discard (5)
print(set2,'\n')

# 5- Phương thức copy 
'''         Cú pháp : <Set>.copy()
            Trả về 1 bản sao của Set
'''

set3=set2.copy()
print(set3,'\n')

# 6- Phương thức add
'''         Cú pháp : <Set>.add(value)
            Thêm value vào set , nếu value đã có trong set rồi thì bỏ qua 
'''
set3.add(5)
print(set3,'\n')

''' IIII- Set không phải là 1 hash object
'''
set4={1,2,3}
print(id(set4),'\n')

set4.add(4)
print(id(set4),'\n')
# ===> Ta thấy id của set4 không thay đổi sau khi ta thêm vào phần tử 4 nên set không phải là 1 hash object

''' Bài tập :  Giai thích tại sao có sự thay đổi ở set a ? cho giải pháp khắc phục
             a = {1, 2}
             b = a
             b.clear()
             a # tại sao lại trở thành set rỗng?
            set()
'''
''' a trỏ thành set rỗng vì set như là 1 con trỏ , khi ta gán b=a nghĩa là ta dùng con trỏ b trỏ đến địa chỉ 
        của set a , nên mọi thay đổi ở b cũng chính là thay đổi ở a
'''
# Fix :
a={1,2}
c=a.copy()
b=c
b.clear()
print(b,'\n')
print(a,'\n')