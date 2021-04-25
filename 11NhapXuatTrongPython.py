'''                     HÀM XUẤT TRONG PYTHON

I - Sử dụng hàm Print thông qua các Parameter 
    Cú pháp : print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
'''

# 1- Parameter  *object :
''' 
    Chính là packing argument : có nghĩa là nó sẽ gom lại các argument thành 1 Tuple
'''
packing1 = 1,2,3,4,5,6
# parameter *object sẽ gom các argument vào thành 1 tuple 
print(packing1)

# Khi bạn truyền các argument vào hàm (giá trị 1, giá trị 2, .... ) nó sẽ gói lại thành 1 Tuple 
print('Nghiem','Anh',2010)

# Nhờ việc gom lại thành 1 tuple bạn có thể truyền argument vào hàm print với số lượng bất kì 
#   ta sẽ ko cần phải ép kiểu dữ liệu ,để rồi nối chúng lại với nhau thành 1 giá trị rồi mới truyền cho hàm print
print('Quang'+'Anh'+str(2010))
print('Quang','Anh',2010)
print((1,2,3),[7,6,5],'Anh')

#   2- Parameter sep (separate - chia ra , phân ra)
''' 
    Gía trị mặc định của parameter này là 1 khoảng trắng 
    Khi các argument bạn ném vào cho hàm print để hàm print in ra nội dung , nó sẽ được gom lại thành 1 Tuple 
        và các phần tử trong Tuple sẽ được nối với nhau bằng Parameter Sep
'''
print('Nghiem','Ba','Quang','Anh')      # Sep mặc định là 1 khoảng trắng 
print('Nghiem','Ba','Quang','Anh',sep='---')    # Sep là ---
print('Nghiem','Ba','Quang','Anh',sep='\n')

# 3- Parameter End ( Kết thúc bằng )
'''         Trong Python thì mỗi lần print chúng sẽ tự xuống dòng . Đó là nhờ Parameter end , nó sẽ tự thêm 1 ký tự
    newline(\n) vào cuối để đưa con trỏ xuống dòng mới thay vì bạn pải tự thêm '\n'
        Chúng ta cũng có thể thay đổi giá trị của parameter end này 
'''
print('Hello .My name is QA',end='|||')
print('Nghiem Ba Quang Anh',end='=>>')
print('\n')

'''     Có vài vấn đề với việc sử dụng hàm print mà ko có newline(\n)
'''

# Nhận hàm sleep từ thư viện time 
from time import sleep 
#print('start....')
#sleep(3)        # Dừng chương trình lại 3s
#print('end....')

# => Chạy chương trình này thì ta thấy xuất hiện dòng start.... và 3s sau thì xuất hiện dòng end....

print('start....',end='',flush=True)
sleep(3)
print('end....')

# Một số ví dụ 
print('line1\n','line2',end=' ')
sleep(3)
print('end....')

# 4-Parameter file :
'''
    Hàm print mặc định sẽ ghi nội dung vào file sys.stdout . Nhờ vậy bạn mới thấy được nội dung trên shell 
        dựa vào đây ta có thể sử dụng hàm print như phương thức Write trong viêc ghi file
'''
with open('file2.txt','w') as file_object1 :
    print('Hello, Welcome to your text',file=file_object1)
with open('file2.txt') as file_object1:
    data1=file_object1.read()
print(data1)

# 5- Parameter flush 
'''     
    Parameter cuối cùng - flush. Giá trị mặc định giá trị là False. Liên quan khá nhiều đến parameter end
        lúc nãy thế nên ta hãy quay lại ví dụ lúc nãy.
    Nếu là True, nó sẽ yêu cầu bộ đệm xuất những gì có trong bộ đệm ra.
'''        