'''                         LIST trong python
I- List là 1 container được sử  dụng rất nhiều trong các chương trình Python 1 list gồm các yếu tố sau:
    1-Được giới hạn bởi ngoặc [ ] , tất cả những gì nằm trong nó là những phần tử của list 
    2- Các phần tử của list được phân cách bởi dấu ,
    3- List có khả năng chứa mọi giá trị ,đối tượng trong python ,Và bao gồm cả chính nó
II-Khởi tạo list :
    Sử dụng dấu ngoặc [<giastri 1> , <giastri 2]>,,,,,]
'''
'''
III-Sử dung list comprehension
    cú pháp : [ comprehension]
    vd: s=[i for i in range(5)]
        => s=[0,1,2,3,4]
        s1=[[n,n+1,n+2] for n in range(2,6)]
        => s1=[[2,3,4] , [3,4,5], [4,5,6], [5,6,7]]
'''
s=[i for i in range(5)]
s1=[[n,n+1,n+2] for n in range(2,6)]
print(s,'\n')
print(s1,'\n')

'''
IIII- Sử dụng contructor list:
    Cú pháp : list(iterable)
    iterable là một đối tượng nói chung của các container.
'''
l1='QuangAnh'
print(list(l1),'\n')

'''  ------------------------------------------------------------------------------------------   
                                MỘT SỐ TOÁN TỬ VỚI CHUỖI
'''

# Toán tử + : 1 list + 1 chuỗi sẽ cho ra list mới gồm các phần tử của cả list và chuỗi
lst1='Nghiem '
lst1 += 'Anh'
lst2= ' Ba Quang '
print(lst1,'\n')
print(lst1 + lst2,'\n')
# Lưu ý : Không thể + 1 chuỗi với 1 list : 'abc' + lst1 = error

# Toán từ *: 
lst3= 'Anh'
lst4=lst3 *2
print(lst4,'\n')

# Toán tử in : Trả về True nếu 1 chuỗi được tìm thấy trong 1 list và False nếu ngược lại
c1='anh'
c2='nghiem ba quang anh'
print(c1 in c2,'\n')

# Indexing và cắt List trong Python
lst5=[1,2,3,'a','b',['d',4]]
print(lst5[0],'\n')
print(lst5[-1],'\n')        # => ['d', 4]
print(lst5[0:5:2],'\n')     # => [1, 3, 'b']
print(lst5[1:3],'\n')

# Thay đổi nội dung List trong Python
'''     Đối với chuỗi ta không thể thay đổi nội dung của chuỗi 1 cách trực tiếp , nhưng đối với list ta có thể
thay đổi nội dung của chuỗi
'''
lst6=[1,2,3,4,5,6]
print(lst6[2],'\n')
lst6[2]='a'
print(lst6[2],'\n')

# Ma Trận 
lst7=[[1,2,3] , [4,5,6]]
print(lst7,'\n')
print(lst7[0],'\n')     # Xuất ra hàng thứ 0 của ma trận
print(lst7[0][2],'\n')  # Xuất ra phần tử ở vị trí hàng 0 cột 2
print(lst7[0][:2],'\n') # Xuất ra các phần tử ở hàng 0 cột 0 và 1
print(lst7[1][:],'\n')  # Xuất ra tất cả các phần tử ở hàng 1

# Vấn đề cần lưu tâm khi sử dụng chuỗi
'''     Ta không được phép gán 1 list này qua list khác vì list như là 1 con trỏ 
    khi gán list này cho list khác có nghĩa là trỏ vào địa chỉ của list đó nên mọi thay đổi của list này cũng là 
    thay đổi list kia
'''
lst8=[1,2,3,4,5,6]
lst9=lst8
print(lst9,'\n')
lst9[3]='a'         # Mọi thay đổi trong lst9 cũng là thay đổi trong lst8
print(lst8,'\n')    #=>[1, 2, 3, 'a', 5, 6]

# Ta nên copy gia trị của list trước khi gán
# Cách 1:
lst10= list(lst8)   
print(lst10,'\n')
lst10[3]=4
print(lst8,'\n')

# Cách 2:
lst11=lst8[:]       # Gán các giá trị trong lst 8 vào lst11
print(lst11,'\n')
lst11[3]=4
print(lst8,'\n')

# Bài tập:
'''1 - Khởi tạo các list sau:  list(list(list('abc'))
                                [1, 2, 3] + list(4)
                                list()
                                [0] * 3
'''
bt1=list('abc')     # = list(list(list('abc'))
print(bt1)
print(bt1.append('d'))

