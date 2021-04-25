'''
    I - Unpacking argument với * 
'''

# Ta có 1 hàm sau :
def qanh(a,b,c,d):
    print(a,b)
    print(c,d)

# Thông thường ta phải gọi hàm này thì pải đưa 4 argument vào 
qanh(1,2,3,4)

# Nhưng nếu argument cần truyền vào nằm trong 1 list thì :
list1=['ANH',20,'HY','Man']
# Ta có thể dùng dấu * 
qanh(*list1)

'''     Khi bạn sử dụng * , bạn ko chỉ có thể unpacking được các list mà bên cạnh đó bạn có thể unpack các
    container khác như Tuple , Chuỗi ,Generator , Set,Dict(chỉ lấy được key)
        Pass argument bằng cách unpacking argument này là ta đang truyền vào dưới dạng positional argument 
    hãy chú ý hàm có parameter dạng keyword only argument 
'''
#   II- Packing argument với * 
'''         Hàm print có khả năng nhận bao nhiêu argument cũng được nhờ packing argument 
        Nhiều khi ta ko biết trước được sẽ pass vào bao nhiêu argument , việc kiểm soát là ko thể
        Khi sử dụng packing argument có nghĩa là ta nhờ 1 biến đi gói tất cả các value truyền vào hàm 
            bằng positional argument thành 1 Tuple . Để giao nhiệm vụ này cho 1 biến ta sử dụng dấu * đặt trước nó
'''
def qanh (*args):
    print(args)
    print(type(args))

qanh('ANH',20,10,2001,'HUNG YEN')
# unpacking argument sau đó packing argument 
qanh(*(x for x in range(5)))
# 1-Ko được phép để 2 parameter cùng làm nhiệm vụ packing arguments trong cùng 1 hàm
'''
  2- Nếu sau 1 packing parameter còn có những parameter khác ,khi gọi hàm muốn truyền giá trị vào cho các 
    parameter sau khi packing argument ta cần phải sử dụng keyword arguments
'''
def nbqa(*anh,key1):
    print(anh)
    print(key1)
list2=['QANH',20,'HY']
nbqa(*list2,key1='PRO')

#      III- Unpacking argument với dấu **
'''         Với việc unpacking 1 dict với dấu * thì ta chỉ có thể lấy các key của dict thôi
            Muốn lấy cả key và value của 1 Dict thì ta cần phải dùng dấu **
            Nếu bạn unpacking 1 Dictionary để truyền argument vào cho hàm khi gọi hàm thì đây chính là 
                keyword argument . Vậy nên bạn phải chắc chắn rằng parameter và key phải giống nhau
'''
dict1={'name':'QANH','age':20}
def dictF(name,age):
    print(name,age)
dictF(**dict1)

#       IV- Packing argument với dấu **
'''         Khác với dấu * là gói những positional argument thì ** lại gói các keyword argument trong 1 dict
'''
def packing1(**arrrr):
    print(arrrr)
packing1(name='Minh',age=21)
