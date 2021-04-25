'''
                        Hàm Nhập Input
    Cú pháp : input( promtpt=None)
    Parameter prompt là một parameter tùy chọn. Bạn có thể nhập hoặc không vì nó đã có giá trị mặc
        định là None.
    Hàm này giúp chúng ta đọc 1 chuỗi từ standard input nghĩa là ta nhập dữ liệu trên Shell sau đó trả về cho
        chúng ta .Vì nó là đọc 1 chuỗi nên dù bạn có nhập vào là gì đi nữa list, tuple set,dictionary,...thì nó 
        vẫn là 1 chuỗi 
    Việc nhập sẽ kết thúc sau khi bạn nhấn phím Enter
    Nếu promtpt khác None ,có nghĩa là bạn gửi cho promtpt 1 giá trị .Thì giá trị này sẽ được in ra mà ko có kí tự
        newline đi kèm trước khi đọc giá trị nhập vào 
'''
value1=input()          # Nhập dữ liệu vào với promtpt mặc định
print('First value is :',value1)

value2=input('first value is :')
print(value2)

name=input('Please enter your name :')
print(name)

int_num=input('Enter a int number :')
float_num=input('Enter a float number :')
lst = input('Enter a list :')
tup = input('Enter a tuple:')
set1=input('Enter a set :')
dict1=input('Enter a dict:')

print('Type of int_num:',type(int_num))
print('Type of float_num :',type(float_num))
print('Type of lst :',type(lst))
print('Type of tup :',type(tup))
print('Type of set1:',type(set1))
print('Type of dict1 :',type(dict1))