'''
                                I-CÁC PHƯƠNG THỨC BIẾN ĐỔI 
'''

# 1- Phương thức capitalize : Trả về 1 chuỗi với kí tự đầu tiền được viết hoa và viết thường tất cả các kí tự còn lại
s="nghiem ba quang anh"
s1=s.capitalize()
print(s1,'\n')

# 2- Phương thức Upper() : Trả về 1 chuỗi với tất cả các kí tự đều được viết hoa
s2=s.upper()
print(s2,'\n')

# 3- Phương thức Lower() : Trả về 1 chuỗi với tất cả các kí tự đều được viết thường
s3=s2.lower()
print(s3,'\n')

# 4- Phương thức swapcase() : Trả về chuỗi với các kí tự viết hoa thành kí tự viết thường , kí tự viết thường thành viết hoa
s4="Nghiem Ba Quang Anh"
s5=s4.swapcase()
print(s5,'\n')

# 5- Phương thức title(): Trả về 1 chuỗi với định dang tiêu đề ,có nghĩa là các từ sẽ được viết hoa chữ cái đầu tiên
s6=s.title()
print(s6,'\n')

'''                         II-CÁC PHUONG THỨC ĐỊNH DẠNG
'''

# 6- Phương thức center(width,[fillchar])  
'''Trả về 1 chuỗi được căn giữa với chiều rộng width
        Nếu fillchar là none thì sẽ dùng kí tự khoảng trắng để căn 
        Nếu fillchar khác none thì sẽ dùng fillchar đó để căn
        Với fillchar là chuỗi có độ dài 1 kí tự
'''
# Căn giữa với độ rộng là 20
f1='quanganh'.center(20)
print(f1,'NBQA\n')
f2='nbqa'.center(20,'*')
print(f2,'qanh\n')

# 7-Phương thức rjust()
'''     Cú pháp : rjusst(width, [fillchar])
        Trả về 1 chuỗi được căn lề phải
'''
# 8-Phương thức ljusst()
'''     Cú pháp : ljust(width,[fillchar])
        Trả về 1 chuỗi được căn lề trái
''' 

''''                       III-Các phương thức xử lí
'''

# 1- Phương thức encode(encoding=’utf-8’, errors=’strict’) - Mã hóa()
'''     Đây là phương thức dùng để mã hóa 1 chuỗi với phương thức mã hóa mặc định là utf-8. Còn về errors mặc định
    là strict có nghĩa là sẽ thông báo lỗi nếu có vấn đề xuất hiện trong quá trình encode chuỗi 
'''
e1='có gì hót'
e2=e1.encode()
print(e2,'\n')

# 2-Phương thức join() 
'''     Cú pháp : <kí tự nối>.join(<iterable>)
        Trả về 1 chuỗi bằng cách nối các phần tử trong iterable bằng kí tự nối .
        Phương thức này được dùng để nối một tập hợp thành một chuỗi sử dụng kí tự cho trước
'''
lst = ['Nghiem','Ba','Quang','Anh']
print(" ".join(lst),'\n')
print(' '.join(['1','2','3','4']),'\n')

# 3-Phương thức repalce :
'''     Cú pháp : <chuỗi>.replace(old,new,[count])
        Trả về 1 chuỗi với các chuỗi old nằm trong chuỗi ban đầu được thay thế bằng chuỗi mới new. Với count là số
        lần lặp lại việc thay thế 
'''
rp1='Nghiem ba quang anh'
rp2=rp1.replace('a','A')        # Thay thế toàn bộ kí tự 'a' thành 'A' 
print(rp2,'\n')

rp3=rp1.replace('a','A',2)      # Thay thế 2 lần kí tự 'a' thành 'A'
print(rp3,'\n')

# 4- Phương thức strip()
'''         Cú pháp : <chuỗi>.strip([chars])
            Trả về 1 chuỗi với phần đầu và phần cuối của chuỗi được bỏ đi các kí tự char
            Nếu chars bị bỏ trống thì các kí tự mặc định bị bỏ đi là khoảng trống và các Escape sequence
            Một số escape sequence ngoại lệ như \a
'''
st1 = '   QUANG  ANH   '
st2=st1.strip()
print(st2,'\n')
st3='******ANH******'
st4=st3.strip('*')
print(st4,'\n')

# 5-Phương thức rstrip()
'''         Cú pháp: <chuỗi>.rstrip([chars]) 
            Cách dùng như strip() , khác là chỉ bỏ đi ở phần đuôi từ phải sang trái
'''
# 6-Phương thức lstrip() 
'''       Cú pháp:  <chuỗi>.lstrip([chars])
          Khác là chỉ bỏ đi các lí tự chars ở phần đầu từ trái qua phải
'''