'''
    I-CÁC PHƯƠNG THỨC TIỆN ÍCH
'''
# 1-Phương thúc count()
'''     Cú pháp :<List>.count(sub, [start, [end]])
        Công dụng : Giong với phương thức count của kiểu chuỗi
        Trả về 1 số nguyên là số lần xuất hiện của sub trong list
'''
# 2- Phương thức copy()
''' 
    Cú pháp : <list>.copy()
    Trả về 1 list tương ứng với List[:]
'''
lst1=[1,2,3,4,'a']
lst2=lst1.copy()
print(lst2,'\n')

# 3-Phương thúc clear
''' Cú pháp : <List>.clear()
    xóa mọi phần tử có trong list
'''
print(lst1.clear(),'\n')

'''    II - CÁC PHƯƠNG THỨC CẬP NHẬP 
'''
# 1-Phương thúc append()
'''     Cú pháp : <List>.append(x)
        Công thêm phần tử x vào cuối list
'''
lst5=[1,2,3,4]
lst5.append('a')
print(lst5,'\n')

# 2-Phương thức extend()
'''         Cú pháp :<List>.extend(iterable)
            Thêm từng phần tử của iterable vào cuối list 
'''
lst6=lst5[:]
lst7=[5,6,7,8]
lst6.extend(lst7)           # Với iterable là 1 list
print(lst6,'\n')

c1='Anh'
lst5.extend(c1)             # Với iterable là 1 chuỗi
print(lst5,'\n')

# 3-Phương thức insert()
'''     Cú pháp : <List>.insert (i, x)
        Thêm phần tử x vào vị trí i của list
'''
lst8=[1,2,3,4,5]
lst8.insert(3,'a')      # Thêm phần tử 'a' vào trị trí thứ 3+1
print(lst8,'\n')

# Nếu i mà lớn hơn độ dài của list thì sẽ tự động thêm phần tử đó vào cuối list

lst8.insert(8,'b')
print(lst8,'\n')

# Nếu i âm thì sẽ thêm phần tử x vào vị trí i-1
lst8.insert(-1,'c')     # Thêm phần từ 'b' vào vị trí -2 của list
print(lst8,'\n')
# Nếu i âm và i nằm ngoài kích thước list thì sẽ tự động thêm x vào vị trí đầu tiên của list
lst8.insert(-12,'Q')
print(lst8,'\n')

# 4-Phương thức pop()
'''         Cú pháp : <List>.pop([i])
            Bỏ đi phần tử thứ i trong list và Trả về giá trị đó .
            Nếu vị trí i ko được cung cấp thì phương thức này sẽ bỏ đi phần tử cuối cùng trong list và trả về giá 
                trị đó
'''
st1=[1,2,3,4,5,'a']
st2=st1.pop(3)      # Bỏ đi phần từ ở vị trí thứ 3 trong st1 và trả về phần tử đó
print(st2,'\n')
print(st1,'\n')

# 5-Phương thức remove
'''     Cú pháp : <List>.remove(x)
        Bỏ đi phần tử đầu tiền trong List có giá trị x 
        Nếu list không có giá trị x thì sẽ có lỗi được thông báo
'''
st3=[1,2,3,1,5,2,7]
st3.remove(2)   
print(st3,'\n')

'''     III-CÁC PHƯƠNG THỨC XỬ LÍ 
'''
# 1-Phương thức reverse()
'''         Cú pháp : <List>.reverse()
            Đảo ngược các phần từ trong list
'''
st4=[1,2,3,4,5,6]
st4.reverse()
print(st4,'\n')

# 2-Phương thức sorted()
'''         Cú pháp : <List>.sort(key=None, reverse=False)
            Nếu reverse = True thì là sxep từ lớn đến bé và ngược lại nếu reverse=Fale
            Mặc định sắp xếp các phần tử từ bé đến lớn bằng cách so sánh trực tiếp
            Key : tùy chọn , nếu có hàm sorted sẽ so sánh với giá trị key sau đó sắp xếp 
'''
st5=[7,98,24,1,2,8,11,4,5]
st5.sort()                      # Sắp xếp list st5 từ bé đến lớn
print(st5,'\n')

st6=['anh','ba','quang','nghiem']
st6.sort()                          # Ta cũng có thể so sánh rồi sắp xếp chuỗi          
print(st6,'\n')
# Với key khác None :

def take_second(elem):                          # Sắp xếp dựa trên phần tử thứ 2
        return elem[1]       
random=[(2, 2), (3, 4), (4, 1), (1, 3)]         # list ngẫu nhiên
list_sort=sorted(random, key = take_second)      # sxep list với key
print(list_sort) 

# List kết quả thi học kỳ của các sinh viên
# Các thành phần của list: (Tên sinh viên, Điểm số đạt được theo thang 100, Tuổi)
participant_list = [
    ('Lê An', 50, 18),
    ('Trần Bình', 75, 12),
    ('Trần Bình', 75, 20),
    ('Thanh Lam', 90, 22),
    ('Lê An', 45, 12)
]
# Gio ta cần sắp xếp ds sinh viên theo thứ tự tên > điểm > tuổi
# Ta làm được điều này với hàm sorted() với nhiều key bằng cách đưa con số về dạng tuple
# 2 Tuple có thể được so sánh bằng cách so sánh các yếu tố từ đầu đến cuối .Nếu có 1 yếu tố bằng(n) , yếu tố thứ 2 sẽ được so sánh ...
def sorter(tup1):
        return (tup1[0],tup1[1],tup1[2])
new_list=sorted(participant_list,key=sorter)
print(new_list)        
# Không thể so sánh và sắp xếp 1 list có cả chuỗi và số