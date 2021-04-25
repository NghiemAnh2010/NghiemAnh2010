''''                Cấu Trúc Vòng Lặp While 
1- Cú pháp : while expression:
                # while block
'''

# 2 - Sử dụng vòng lặp để xử lí chuỗi list,tuple
s='Nghiem Ba Quang Anh'
idx=0
while idx < len(s):
    print(idx,s[idx])
    idx+=1

# 3- Câu lệnh break 
'''         Dùng để kết thúc vòng lặp , nó nằm trong block của vòng lặp nào thì vòng lặp đó kết thúc khi chạy 
    câu lệnh này 
'''
lst1=[]
idx1=0
while 1:
    if idx1 % 2==0 :
        lst1.append(idx1)
    if len(lst1)==5 :
        break
    idx1+=1
print(lst1)

# 4- Câu lệnh continue:
''' Câu lệnh này dùng để tiếp tục vòng lặp 
    Câu lệnh sẽ bỏ qua mọi block ở dưới nó và tiếp tục vòng lặp 
'''
numb1=1
while numb1 <10:
    if numb1 %2 ==0:
        numb1+=1
        continue
    print(numb1,'is odd number')
    numb1+=1

# 5-Cấu trúc vòng lặp while-else 
'''     Cú pháp :   while expression :
                        # while block
                    else :
                        # else block
            Khi vòng lặp while kết thúc thì khối lệnh while block sẽ được thực hiện
'''
# Bài tập:
with open('draft.txt') as file_object:
    data1=file_object.readlines()   # Lấy nội dung của file dưới dạng 1 list  
idx=0
list_new=[]
new_contens=''
while idx<len(data1):
    list_new=data1[idx].split()
    i=0
    while i < len(list_new):
        if list_new[i] == 'Kteam':
            list_new[i-1]='How'
        i+=1
    new_contens+=' '.join(list_new)+'\n'
    idx+=1

with open('kteam.txt','w') as file_object1:
        file_object1.write(new_contens)
file_object1=open('kteam.txt')
data2=file_object1.read()
print(data2)