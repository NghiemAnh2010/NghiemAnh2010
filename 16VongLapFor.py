'''                     Cấu Trúc Vòng Lặp For
    I-Cú Pháp : for variable 1, variable 2,... in sequence
                    # for-block
        Sequence ở đây là 1 iterable object 
        Nếu iterable là 1 iterator object thì dùng vòng lặp duyệt cũng tương tự như dùng hàm next để duyệt
'''
''' II- Sử dụng vòng lặp để xử lí các iterator và Dict 
'''
# 1- Với iterator :
iter1 = (x for x in range(5))
for i in iter1:
    print(i)

# 2-Ta duyệt 1 Dict :
# Dict-items ko phải là 1 iterator object .Cũng ko phải 1 object cho phép bạn indexing .Nhưng nó vẫn là 1 iterable
dict1={'name':'QaNH','age':20}
# Ta dùng 2 contructor list để biến đổi nó về dạng dễ xem xét hơn
list1=list(dict1.items())
for i in list1:
    print(i)

# Ta có thể dễ dang duyệt 1 dict như sau:
for key,value in dict1.items():
    print(key,'->',value)

'''     Cấu trúc vòn For - Else
    Tương tự như vòng while -else
'''

'''     Bài Tập củng cố 
1: iter_ = (x for x in range(3))
     for value in iter_:
         print(non_exist_variable)
next(iter_)
    Dự đoán kết quả ?
2 :Sử dụng vòng lặp để tính tổng các số trong set sau đây
    set_={5,8,1,9,4}
'''
set_={5,8,1,9,4}
result=0
for i in set_:
    result+=i
print(result)

    
