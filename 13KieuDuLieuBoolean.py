'''                         KIỂU DỮ LIỆU BOOLEAN
Boolean là kiểu dữ liệu chỉ có 2 giá trị True và False
'''

# 1-Toán tử so sánh :
    #1.1 : So Sánh dạng số
print(5>4)
print(5*0 != 0)
    # 1.2: So sánh giữa 2 iterable cùng loại 
print('Qanh'=='Qanh')
result='Qanh'=='QANH'
print(result)
    # Khi so sánh các kí tự với nhau = cách đưa chúng về dưới dạng số bằng hàm ord .Bạn có thể tham khảo giá trị 
    #   của nó trong ASCII Table
print(ord('A'))
print(ord('a'))

# 2-Toán Tử is :
'''         So sánh bằng toán tử == nghĩa là ta đi so sánh bằng giá trị 
            Còn nếu so sánh bằng toán tử is thì Python sẽ lấy giá trị của hàm id để so sánh
'''
lst1=[1,2,3,4,5]
lst2=[1,2,3,4,5]
print(lst1==lst2)

# Tại đây 2 list này đang trỏ chung vào 1 địa chỉ
lst3=lst1
print(lst3 is lst1)

''' Lưu ý : Các số từ -5 đến 256  hoặc 1 chuỗi có số kí tự <20 thì các biến có cùng 1 giá trị sẽ có cùng 
        1 giá trị trả về từ hàm id
'''
a=4
b=4
print(a is b)
c=990
d=990
print(c is d)

# NOT ,AND ,OR trong python
'''     Các giá trị cũng là các boolean 
        + Số 0 , None , Rỗng là các giá trị False 
'''

# Syntaxnic sugar cho việc so sánh 

# Xác định x có nằm trong 1 khoảng nào đó k ?
x=5
print(1<x<4)

x1=9
check= 0<x<6<10<x1
print(check)

# Xét TH k có bằng x , y , z hay k 
k=4
check1=k in (1,4,9)
print(check1)