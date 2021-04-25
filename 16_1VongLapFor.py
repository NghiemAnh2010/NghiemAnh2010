'''                     Kiểu Dữ Liệu Dãy Số Range
'''
# Cách khởi tạo thứ 1:
'''     Cú pháp : range(stop)
'''
a=range(4)
print(type(a))
print(a)
print(a[1])


# Cách khởi tạo thứ 2:
'''      Cú pháp : range(start,stop,step)
'''
k=list(range(0,10,2))
k1=list(range(2,-3,-1))
print(k)
print(k1)

#                       *** Sử dụng range để duyệt 1 List,tuple,chuỗi ***
lst=['s',(1,2,3),{'abc','xyz'}]
for i in range(len(lst)):
    print(lst[i])
''' Comprehension là công cụ rất hiệu quả của Python để xủ lí rất nhiều việc mà bạn chỉ cần 1 dòng
    Comprehension còn giúp code trở lên nhanh hơn
 Cú pháp : [output-expression for -statement optional-predicate]
'''

#                       ******** KO sử comprehension ********
lst1=[]
for a,b,c in [('how','kteam','EDUCATION'),('chia','se','FREE')]:
    a=a.capitalize()
    b=b.upper()
    c=c.lower()
    lst1.append('--'.join((a,b+c)))
print(lst1)

# Sử dụng comprehension 
lst2=['--'.join((a.capitalize(),b.upper() + c.lower())) for a,b,c in [('how','kteam','EDUCATION'),('chia','se','FREE')]]
print(lst2)

# VD2 Ko sử dung comprehension 
dict2={}
for key,value in (('Qanh',21),('NBQA',20),('age',2001),('mark',90)):
    if value % 2 !=0:
        dict2[key]=value+1
print(dict2)

# Sử dung comprehension
dict3={key:value+1 for key,value in (('Qanh',21),('NBQA',20),('age',2001),('mark',90)) if value % 2 !=0}
print(dict3)

'''                             Hàm Enumerate
    Cú pháp : enumerate(iterable,start)
    Nếu start ko được gửi vào thì mặc định là 0
    Hàm này là 1 generator nhờ câu lệnh yield trong hàm .Nó sẽ tạo ra mỗi giá trị là 1 cặp gồm số thứ tự và giá trị
        của nó
'''
student_list = ['Long', 'Trung', 'Giàu', 'Thành']
new_student=enumerate(student_list,4)
print(new_student)
print(list(new_student))

# Ta có thể sử dụng trong vòng for :
for idx,value in enumerate(student_list):
    print(idx,'=>',value)

''' Bài Tâp củng cố
1.Sử dụng sequence scan để thay đổi phần tử đầu tiên của mỗi phần tử trong List dưới đây thành None
    lst = [[1, 2, 3], [4, 5, 6]]
'''
lstBT = [[1, 2, 3], [4, 5, 6]]
print(lstBT[0])
for a in lstBT:
    a[0]=None
print(lstBT)

''' 2 :
'''
n=int(input('Nhap so hang va so cot cua ma tran :'))
m=(n**2)
print(m)
x,y=1,0
print(x,y)
strix=[[None]*n for j in range(n)]
print(strix)