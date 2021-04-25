'''
                         I-CÁC PHƯƠNG THỨC TÁCH CHUỖI 
'''

# 1- Phương thức split
'''     Cú pháp : <chuỗi>.split(sep=None, maxsplit=-1)
        Trả về 1 list bằng cách chía các phần tử trong chuỗi ban đầu bằng kí tự sep
        Nếu sep =None thì sẽ dùng kí tự khoảng trắng
        Nếu maxsplit mặc định =-1 , Python sẽ không bị giới hạn việc tách ,còn không Python sẽ tách với số lần được
            cung cấp thông qua maxsplit
'''
s1='Nghiem Ba Quang Anh'
# Tách chuỗi s1 với sep và maxsplit mặc định
s2=s1.split()
print(s2,'\n')

# Tách chuỗi s1 với maxsplit =2 và sep mặc định
s3=s1.split(maxsplit=2)
print(s3,'\n')

s4='Nghiem-Ba-Quang-Anh'
# Tách chuỗi s1 với sep='-' và maxsplit=2
s5=s4.split(sep='-',maxsplit=2)
print(s5,'\n')

# 2- Phương thức rsplit():
'''         Cú pháp: <chuỗi>.rsplit(sep,maxsplit)
            Công dụng cũng hoàn toàn như split nhưng việc tách được thưc hiện từ phải sang trái
'''

# 3 -Phương thức partition():
'''     Cú pháp : <chuỗi>.partition(sep)
        Trả về 1 tuple với 3 phần tử .Các phần tử đó lần lượt là chuỗi : trước chuỗi sep , sep , chuỗi sau sep
        Trong trườn hợp không tìm thấy sep trong chuỗi thì mặc định trả về giá trị đầu tiên là chuỗi bân đầu , 2 
            giá trị tiếp theo là rỗng
'''
p1='Hello Nghiem Ba Quang Anh 2010'
p2=p1.partition('Nghiem')
print(p2,'\n') 

p3=p1.partition('Nghi')
print(p3,'\n')

p4=p1.partition('pro')
print(p4,'\n')

# 4-Phuong thức rpartition():
'''         Cú pháp : <chuỗi>.rpatition(sep)
            Cũng giống như partition() nhưng lại chia các phần tử từ phải qua trái
'''

'''                        II-CÁC PHƯƠNG THỨC TIỆN ÍCH
'''

# 1-Phương thức count():
'''         Cú pháp: <chuỗi>.count(sub, [start, [end]])
            Trả về 1 số nguyên ,chính là số lần xuất hiện của sub trong chuỗi .Cón start và end là số kĩ thuật 
                slicing
'''
c1='nghiem ba quang anh'
# Cho ra số lần xuất hiện kí tự 'n' trong chuỗi c1 với vị trí bắt đầu là từ đầu chuỗi và kết thức ở cuối chuỗi
c2=c1.count('n')
print(c2,'\n')

c3='aaaaaaa'
# Cho ra số lần xuất hiện kí tự 'a' trog chuỗi c3 với vị trí bắt đầu tìm là vị trí thứ 3 trong chuỗi c1
c4=c3.count('a',3)
print(c4,'\n')

c5=c3.count('a',0,5)
print(c5,'\n')

#  2- Phương thức stratswith():
'''         Cú pháp : <chuỗi>.startswith(prefix[, start[, end]])
            Trả về giá trị True nếu chuỗi đó bắt đầu bằng chuỗi prefix. Ngược lại là False
            Hai yếu tố start, end tượng trưng cho việc slicing (không có bước) để kiểm tra với chuỗi slicing đó.
'''
st1='hello nghiem ba quang anh'
st2=st1.startswith('hel')
print(st2,'\n')

st3=st1.startswith('llo')
print(st3,'\n')

st4=st1.startswith('llo',2)
print(st4,'\n')

# 3-Phương thức endswith()
'''         Cú pháp :<chuỗi>.endswith(prefix[, start[, end]])
            Trả về giá trị True nếu chuỗi đó kết thúc bằng prefix và ngược lại
'''

# 4- Phương thức find()
'''         Cú pháp :<chuỗi>.find(sub[, start[, end]])
            Trả về 1 số nguyên là vị trí đầu tiên của sub khi dò từ trái sang phải trong chuỗi , 
            Nếu sub không có trong chuỗi thì kết quả sẽ là -1
            Giong như các phương thức khác ,strat và end đại diện cho slicing
'''
f1='nghiem ba quang anh'
f2=f1.find('a')
print(f2,'\n')

f3=f1.find('ab')
print(f3,'\n')

f4=f1.find('i',7)
print(f4,'\n')

# 5-Phương thức rfind()
'''     Cú pháp :<chuỗi>.rfind(sub[, start[, end]])
        Trả cũng giống như find() nhưng tìm từ phải sang trái
'''

# 6- Phuognw thức index()
'''     Cú pháp : <chuỗi>.index(sub[, start[, end]])
        Công dụng cũng như find() nhưng Nếu không tìm thấy sub trong chuỗi thì sẽ có lỗi ValueError
'''

#7-Phương thức rindex()
'''     Cú pháp :<chuỗi>.rindex(sub[, start[, end]])
        Công dụng y như index() nhưng tìm từ phải qua trái
'''


'''                     III-CÁC PHƯƠNG THỨC XÁC THỰC
'''
# 1-Phương thức islower()
'''     Cú pháp :<chuỗi>.islower()
        Trả về True nếu tất cả ác kí tự trong chuỗi đều đươc viết thường , và ngược là nếu k là False
'''
is1 ='nghiem ba quang anh'
print(is1.islower(),'\n')

is2='Nghiem ba quang anh'
print(is2.islower(),'\n')

# 2- Phương thức isupper()
'''     Cú pháp :   <chuỗi>.isupper()
         Trả về True nếu tất cả các kí tự trong chuỗi đều được viết hoa và False nếu ngược lại
'''
up1='NGHIEM BA QUANG ANH'
up2='nGHIEM BA QUANG ANH'
print(up1.isupper(),'\n')
print(up2.isupper(),'\n')

# 3-Phương thức istitle()
'''     Cú pháp : <chuỗi>.istitle()
        Trả về True nếu chuỗi là 1 dang title() và ngược lại
'''
ti1='Nghiem Ba Quang Anh'
ti2='Nghiem bA Quang Anh'
print(ti1.istitle(),'\n')
print(ti2.istitle(),'\n')

# 4-Phương thức isdigit()
'''     Cú pháp: <chuỗi>.isdigit()
        Trả về True nếu tất cả các kí tự trong chuỗi đều là những con số từ 0-9
'''
di1='12235235085235'
di2='0916615699a'
print(di1.isdigit(),'\n')
print(di2.isdigit(),'\n')

# 5- Phương thức isspace()
'''     Cú pháp : <chuỗi>.isspace()
        Trả về True nếu tất cả các kí tự trong chuỗi đều là khoảng trắng
'''

## Bài tập : dùng các phương thức để biến chuỗi q1 ='Neu Mot Ngay Nao Do'
q1 = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
q2=q1.split('aaaAAaaaooaa',1)       # Tách chuỗi q1 ra tại kí tự'aaaAAaaaooaaa'
q3=q2[1].rsplit('aaaaaaa',1)        
q4=q3[0].lower()
q5=q4.title()
print(q5)

