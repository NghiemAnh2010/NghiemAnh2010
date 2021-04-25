'''             Positional argument và Keywword argument
'''
def function1(a,b):
    pass    # Lệnh giữ chỗ 
function1('QANH',20)
# Trong VD trên 2 giá trị 'QANH' và 20 gọi là positional argument

function1(a='ANH',b=20)
# 2 giá trị trên gọi là keyword argument 
'''     Khi sử dụng positional argument thì có nghĩa là các argument sẽ được gán lần lượt cho các parameter 
    còn đối với keyword thì bạn tự mk gán giá trị cho parameter 
    + Bạn có thể pass positional và keyword cùng 1 lúc nhưng positional buộc pải đứng trước keyword
'''
function1('QANH',b=21)

# Có 1 số hàm bắt buộc chúng ta phải pass argument 1 cách rõ ràng rành mạch như hàm sorted
print(sorted([4,8,3],reverse=True))

#   I- Keyword argument
def Teo(a,b=2,c=3,d=4):         # Khai báo và khởi tạo hàm với các default argument
    f=(a+d)*(c+b)
    print(f)
Teo(1)
# Nếu bạn muốn thay đổi giá trị của paramater d thành 5 thì như sau
Teo(1,d=5)

'''     Cú pháp : def <function_name> ( *,key_arg1 , key_arg2,....)
                        # function-block
        Khi tạo ra 1 hàm có 1 parameter * .Thì python sẽ hiểu đó ko pải là parameter là chính là syntax 
            để rồi nó biến các parameter sau * thành các keyword only argument (chỉ nhận giá trị theo kiểu keyword)
'''
def function2 (name, *,age,address):
    print(name,'=>',age,'=>',address)
function2('Qanh',age=20,address='HY')
