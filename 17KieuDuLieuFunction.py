'''         Lập trình có 2 loại :
    1- Lập trình tuyến tính : Là viết code từ trên xuống dưới , lệnh nào có trước sẽ được thực hiện trước 
    2- Lập trình thử tục : Sử dụng các hàm để code 
'''

# 1 - Khai báo hàm (create function)
'''     Cú pháp : def <function_name> ( parameter1 , parameter2,parameter3....) :
                        function-block 
# 2- Gọi hàm (call function)
        Cú pháp : <function>()
'''
# Khai báo và khởi tạo hàm 
def function1 ():
    print('Hello NBQA!!!')
# Gọi hàm 
function1()

# 3- Parameter và Arrgument
'''         Khi gọi hàm có parameter , bạn phải truyền vào 1 argument tương ứng 
'''
def function2(name,age):
    print(name,age,'!!!')
function2('NghiemAnh',20)

# 4-    Gía trị mặc định của Parameter ( Default argument)
'''         Nếu ta cần 1 parameter giữ được giá trị những vẫn cho ta thay đổi nếu ta cần thì ta nên sử dụng 
                default argument
            Lưu ý : Khi đưa default argument cho các parameter ,pải để các parameter có default argument ở 
                sau cùng 
            Default argument cũng là 1 unhashable container
'''
def function3(name,age=20):
    print(name,age,'!')
function3('NghiemBQA')
function3('NBQA',21)

'''     Ta đã biết 1 số unhashable container phổ biến đã dùng là List , Dict, Set. Lưu ý rằng : 
    Khi ta sử dụng defalut argument cho parameter là 1 unhashable container đó là giá trị của nó sẽ ko được 
    làm mới (refresh) sau mỗi lần gọi hàm mà ko pass argument mới cho parameter đó 
'''
def function4(name=[]):
    name.append('A')
    print(name)
function4()
function4()