'''                     Cấu Trúc Rẽ Nhánh If 
1 - IF : Nếu thì :
    Cú pháp :
            if expression :
                # if-block

2 - if - else if : 
    Cú pháp :
            if expression :
                # if- block
            elif 2-expression :
                # 2 if-block
            elif 3-expression :
                # 3 if-block
            ....
            elif 4-expression :
                # n if-block
            
3- if - else :
    Cú pháp :
            if expression :
                # if -block
            else 
                # else -block
4- if -else if -else 
    Cú pháp :
            if expression :
                # if -block
            elif 2-expression
                # 2-if-block
            ...
            elif n-expression
                # n-if-block
            else 
                # else -block

# II- Block trong Python
    1- Câu lệnh mở block kết thúc bằng dấu 2 chấm (:), sau khi sử dụng câu lệnh có dấu (:) buộc pải xuống dòng 
        và lùi lề vào trong 
    2- Những dòng code cùng lề thì cùng 1 block
    3- Một block có thể có nhiều block khác nhau 
    4- Khi căn lề 1 block ko sử dụng cả tab lẫn space 
    5- Nên sử dụng 4 space để căn lề 1 block
'''

''' Bài tập :
    Nhập từ bàn phím 3 số, in ra số lớn nhất (cố gắng ít dòng code nhất có thể - ở đây không tính việc
        nhập dữ liệu)
'''
a=int(input('Enter number 1:'))
b=int(input('Enter number 2:'))
c=int(input('Enter number 3:'))
max1=a
if max1 <b:
    max1=b
if max1<c:
    max1=c
print('Max =',max1)

# Cách 2:
a1=int(input('Enter number 1:'))
b1=int(input('Enter number 2:'))
c1=int(input('Enter number 3:'))

if a1>b1 and a1>c1 :
    print('Max =',a1)
elif c1>a1 and c1>b1 :
    print('Max =',c1)
else :
    print('Max =',b1)