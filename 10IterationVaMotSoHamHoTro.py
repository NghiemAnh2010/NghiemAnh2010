'''
I -Iteration là 1 khái niệm chúng cho viêc lấy từng phần tử một của 1 đối tượng nào đó , bất cứ khi nào bạn sử
        dung vòng lặp hay kĩ thuật nào đó để có được giá trị 1 nhóm phần tử thì đó là iteration 
II- Iteration object : là 1 object có phương thức __iter__ trả về 1 iterator 
    hoặc 1 object có phương thức __getitem__ cho phép bạn lấy nất kỳ phần tử nào của nó bằng indexing ví dụ như
        Chuỗi , List,tuple
   + Iteration object đơn giản chỉ là một đối tượng mà cho phép ta lấy từng giá trị một của nó. Có nghĩa 
        là bạn không thể lấy bất kì giá trị nào như ta hay làm với List hay Chuỗi.
   + Iterator không có khả năng tái sử dụng trừ một số iterator có phương thức hỗ trợ như file object sẽ
        có phương thức seek.
   + Iterator sử dụng hàm next để lấy từng giá trị một. Và sẽ có lỗi StopIteration khi bạn sử dụng hàm
        next lên đối tượng đó trong khi nó hết giá trị đưa ra cho bạn.
   + Các iterable object chưa phải là iterator. Khi sử dụng hàm iter sẽ trả về một iterator. Đây cũng chính
        là cách các vòng lặp hoạt động.
   + File object cũng là một iterator. Bạn cũng có thể sử dụng cách này để đọc file.
'''
# Tạo 1 list với comprehension
lst1=[x for x in range(4)]
print(lst1,'\n')

# Tạo 1 iterator bằng cách sử dung () cho ra 1 generator object - 1 iterator  
iter1=(x for x in range(4))
print(type(iter1))
# Sử dụng hàm next để lấy từng giá trị ra 
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))      # iter1 chỉ có 4 giá trị và ta đã lấy hết
# Nếu lấy tiếp chuong trình sẽ báo lỗi 

# File object cũng là một iterator. Bạn cũng có thể sử dụng cách này để đọc file.

lst2=[1,2,3,'qanh',2010]
# Tạo 1 iter từ list
iter2=iter(lst2)
print(type(iter2))

# Iterator này cũng dính 1 vấn đề như list ,dict đó chính là chỉnh 1 , thay đổi 2
iter3=iter('NghiemAnh')
print(type(iter3))
iter4=iter3

print(next(iter4))
print(next(iter4))
print(next(iter3))
print(next(iter3))
print(next(iter4))
print(next(iter4))
print(next(iter3))

''''    
    III-Một Số Hàm Hỗ Trợ iterable ibject 
+  Các hàm này buộc phải lấy các giá trị của iterable để xử lí, do đó nếu bạn đưa vào
    một iterator. Thì bạn sẽ không sử dụng iterator đó được nữa
'''
# 1- Hàm tính tổng sum :
'''     Cú pháp : sum(iterable , start = 0)
    Trả về tổng các giá trị của iterable và iterable này chỉ chứa các giá trị là số. Còn start
            chính là giá trị ban đầu. Có nghĩa là sẽ cộng từ start lên. Mặc định là 0
'''
lst3=[1,2,3,4,9,8,7]
print(sum(lst3),'\n')

iter5=(x for x in range(7))
print(next(iter5),'\n')
print(next(iter5),'\n')
print(next(iter5),'\n')

print(sum(iter5))
# Sau khi sử đưa giá trị của iterator vào hàm sum thì ta k còn có thể sử dụng iter5 này nữa 

# 2 -Hàm Tìm Max :
'''         Cú pháp :max(iterable, *[, default=obj, key=func])
        : Nhận vào một iterable.Tìm giá trị lớn nhất bằng key (mặc định là sử dụng operator >)
    Default là giá trị muốn nhận về trong trường hợp không lấy được bất kì giá trị nào trong iterable.
'''
# Tìm max của 1 list
a=max(lst3)
print(a,'\n')
print(max([],default='Qanh'),'\n')
tup1=(5,4,3,1,2)
# Truyền vào hàm max 1 tuple 
print(max(tup1,default='qanh'))

# Hoặc cú pháp khác : max(arg1, arg2, *args, *[, key=func])
'''     . Ở đây không có parameter default, vì khi theo cách này, bạn luôn luôn có ít nhất 2 giá trị so sánh
'''
print(max(20,10,21),'\n')

# 3 - Hàm tim Min:
'''         Cú pháp : min(iterable, *[, default=obj, key=func])
                    Hoặc :min(arg1, arg2, *args, *[, key=func])
        Cũng giống như hàm max
'''

# 4- Hàm sắp xếp - sorted :
'''         Cú pháp :sorted(iterable, /, *, key=None, reverse=False)
             Giống với phương thức sort của List object.
'''
lst4=[5,2,7,9,1]
sorted(lst4)
# Sxep từ bé đến lớn 
print(sorted(lst4),'\n')

# Sxep từ lớn đến bé bằng cách đảo ngược các phần tử 
print(sorted(lst4,reverse=True))

