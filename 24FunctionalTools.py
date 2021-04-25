#  I - Hàm Map 
'''     Cú pháp : map(func,iterable)
        Hàm map này sẽ trả về 1 map object (1 dạng generator)
        Hàm map lấy từng phần từ của iterable  sau đó dùng gọi hàm func với argument là giá trị mới lấy từ iterable
        Kết quả trả về hàm func sẽ được yield
'''
# Hàm map với vc dùng def
def in_x(x):
    return x+1
list1=[1,2,3,4]
lst=list(map(in_x , list1))
print(lst)

# Hàm map với việc dùng lambda
lst1=list(map(lambda x:x+2 , list1))
print(lst1)

'''     Cú pháp đầy đủ của hàm : map(func,*iterable)
    Khi ta muốn pass vào nhiều container cùng 1 lúc thì hàm map sẽ gom lại bằng packing argument thì các container
        phải có cùng số lượng giá trị (cùng giá trị hàm len)
    Vì khi có nhiều container pass vào thì hàm map sẽ cùng 1 lúc lấy lần lượt các giá trị của  các container
'''
func1=lambda x,y: x+y
lst1=[1,2,3,4]
lst2=[5,6,7,8]

lst3=list(map(func1,lst1,lst2))
print(lst3)

#   II- Hàm filter
'''     + Filter có nghĩa là bộ lọc 
        + Cú pháp : filter (function or None ,iterable)
        + Giong như hàm map ,hàm filter sẽ trả về filter object ( 1 dạng generator object)
        + KO như hàm map ,iterable ở đây chỉ là 1 container , ko hề có packing argument
        + Hàm filter dẽ lấy từng giá trị trong iterable sau đó gửi vào hàm , nếu như hàm trả ra 1 giá trị mà 
            chuyển sang kiểu Boolearn là True thì sẽ yield ra giá trị đó , nếu ko thì bỏ qua 
        + Trường hợp function là None thì hàm filter lấy từng giá trị của iterable , nếu giá trị đso chuyển sang Boolearn
            là True thì sẽ yield giá trị đó 
'''
func2=lambda x : x>0
list3=[0,-9,3,5,-6,10,8,6]
filter1=filter(func2,list3)
for i in filter1:
    print(i,end='-')
print('\n')
# Với function là None
filter2=filter(None,list3)
for i in filter2:
    print(i,end='-')
print('\n')

#       III- Hàm Reduce
'''     Là hàm mà bất cứ giá trị nào khi chuyển qua Boolearn mà False thì sẽ ko được Yield
        Hàm reduce nằm trong thư viện functools
        Cú pháp : reduce(function, sequence, initial)
        Hàm reduce trả về 1 giá trị chứ ko phải 1 generator expression
   1- Đầu tiên nếu ko truyền parameter initial vào thì hàm reduce sẽ lấy 2 giá trị đầu tiên của sequence vào hàm 
        function để thực hiện và trả ra 1 giá trị (kiểu giá trị A). Sau đó lấy tiếp giá trị thứ 3 của sequence và 
            giá trị A , tiếp tục như vậy đến khi kết thúc sequence
   2- Nếu ta pass vào argument cho parameter initial thì hàm reduce sẽ lấy giá trị đầu tiên là giá trị của parameter 
        initial mà ta vừa truyền vào
'''
# Lấy hàm reduce từ thư viện functools
from functools import reduce
func3= lambda x,y:x+y
sequence1= [1,2,3,4,5]
result = reduce(func3,sequence1,10)
print(result)
