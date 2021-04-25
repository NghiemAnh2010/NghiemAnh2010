'''
                            Xử Lí File Trong Python
O đây chúng ta chủ yếu xử lí các file text đơn giản
'''

'''
        I-Mở File Trong Python
1- Hàm Open : 
    Để mở 1 file ta sử dụng hàm open 
    Cú pháp : open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Ở mức độ cơ bản ta chỉ quan tâm đến 2 parameter là file và mode 
    Hàm open trả về 1 file object và đây cũng là 1 iterable
2- Các mode cở bản liên quan đến text file:
    r  : Mở để đọc . Đây là mode mặc định
    r+ : Mở để đọc và ghi 
    w  : Mở để ghi .Trước đó nó sẽ xóa hết nội dug của file hiện có 
         Nếu file không tồn tại sẽ tạo ra 1 file với tên file là tên file chúng ta truyền vào
    w+ : Mở để đọc và ghi .Trước đó nó sẽ xóa hết nội dug của file hiện có 
          Nếu file không tồn tại sẽ tạo ra 1 file với tên file là tên file chúng ta truyền vào
    a  : Mở để ghi 
         Nếu file ko tồn tại , sẽ tạo ra 1 file mới với tên file là tên mà ta đã truyền vào 
    a+ : Mở để ghi và đọc 
         Nếu file ko tồn tại , sẽ tạo ra 1 file mới với tên file là tên mà ta đã truyền vào 
'''
file_object = open('file1.txt')
print(file_object,'\n')

#     II-Đóng file 
'''         Cú pháp : <File>.close()
Chúng ta nên đóng file sau khi hoàn tất công việc :
    + Giới hạn hệ điều hành. Chẳng hạn một hệ điều hành chỉ cho mở một số file nhất định cùng lúc
        thì nếu quên đóng file sẽ gây hao tốn. Đặc biệt là các file với dung lượng bự.
    + Khi một file được mở, hệ điều hành sẽ khóa file đó lại, không cho các chương trình khác có thể
        xử lí trên file đó nữa nhằm đảm bảo tính nhất quán của dữ liệu.
'''

#     III-Đọc file :
'''         Cú pháp : <File>.read(size = -1)
    Nếu size bị bỏ trống hoặc là 1 số âm .Nó sẽ đọc hết nội dung của file đồng thời đưa con trỏ file tới 
        cuối file . 
    Nếu không nó sẽ đọc tới n kí tự (với n=size ) hoặc cho tới khi nội dung của file đã đọc xong 
    Sau khi đọc được nội dung , nó sẽ trả về dưới dạng 1 chuỗi 
    Nếu ko đọc được gì , phương thức sẽ trả về 1 chuỗi có độ dài bằng 0
'''
data1=file_object.read()
print(data1,'\n')
print(file_object.read(2),'\n')
# Hiện tại con trỏ file đang ở vị trí cuối cùng của file , bạn ko thê đọc được j nữa và nó sẽ trả về chuỗi rỗng
file_object.close()     # Đóng file

# Mở lại file
file_object1=open('file1.txt')
# Đọc file 
data2=file_object1.read(10)
print(data2,'\n')
 # Đọc hết các kí tự còn lại chưa đọc được của file
print(file_object1.read(),'\n')        
file_object1.close()

# 1 -Phương Thức readline
'''         Cú pháp : <File>.readline(size=-1)
            Với parameter size thì hoàn toàn tương tự như phương thức read.
            Khác biệt ở chỗ, phương thức readline chỉ đọc một dòng có nghĩa là đọc tới khi nào gặp
                newline hoặc hết file thì ngừng.
            Con trỏ file cũng sẽ đi từ dòng này qua dòng khác.
            Kết quả đọc được trả về dưới dạng một chuỗi.
            Nếu không đọc được gì, phương thức sẽ trả về một chuỗi có độ dài bằng 0
'''

# Mở lại file
file_object3=open('file1.txt')
# Đọc file với readline
data3=file_object3.readline()
print(data3,'\n')
print(file_object3.readline(10),'\n')
print(file_object3.readline(),'\n')
file_object3.close()

# 2- Phương Thức Readlines 
'''         Cú pháp : <File>.readlines(hint=-1)
         Phương thức này sẽ đọc toàn bộ file, sau đó cho chúng vào một list. Với các phần tử
            trong list là mỗi dòng của file.
         Con trỏ file sẽ được đưa  tới cuối file. Khi đó, nếu bạn tiếp tục dùng readlines. Bạn sẽ nhận
            được 1 list rỗng
'''
# Mở lại file
file_object3=open('file1.txt')
# Đọc file với readline
data3=file_object3.readlines()
print(data3,'\n')
file_object3.close()

#  3 -Đọc File Bằng Contructor Nhận Iterable
'''         file object nhận được từ hàm open cũng là 1 iterable 
            Thế nên ta có thể sử dụng contructor list hoặc contructor tuple
            Các constructor này cũng sẽ đưa con trỏ file xuống cuối file.
'''
# Mở lại file
file_object3=open('file1.txt')
# Đọc file với contructor list
list_read = list(file_object3)
print(list_read,'\n')
file_object3.close()
# Với contructor tuple cũng tương tự 

'''         IV - Ghi File 
Chúng ta có sự giúp đỡ của phương thức write để ghi nội dung vào file.
Và chúng ta cũng không cần phải tạo file. Vì các mode ghi sẽ giúp chúng ta tạo file.
'''
# 1 -Phương Thức Write 
'''         Cú pháp : <File>.write(text)
      =>   Phương thức này sẽ trả về số kí tự mà chúng ta ghi vào.
            Mỗi lần sử dụng write. Con trỏ file sẽ được đặt ngay sau kí tự cuối cùng được ghi. Hãy lưu ý điều
                này, nó rất quan trọng .Đặc biệt là khi bạn sử dụng các mode vừa đọc vừa ghi.
            
'''
  # Mở file để ghi với mode = 'w'
file_object4=open('file2.txt','w')  
file_object4.write('Hello,My name is Quang Anh\nAge=20')
 # Đòng file ghi này lại
file_object4.close()           

# Mở file để đọc
file_object4=open('file2.txt')
print(file_object4.read(),'\n')
file_object4.close()

# Mở file để ghi với mode = 'w'
file_object4=open('file2.txt','w')  
file_object4.write('Welcom to Your text')
file_object4.close()

# Mở file để đọc
file_object4=open('file2.txt')
print(file_object4.read(),'\n')
file_object4.close()
# ==> Vì ta sử dụng mode ='w' nên các dữ liệu ta đã ghi trước đây bị xóa đi hết 

'''             V - Kiểm Soát Con Trỏ File
    Bạn có thể thấy, con trỏ file rất quan trọng, nó dẫn đường cho việc đọc file, viết file. Và bạn cũng
        cần phải kiểm soát được nó.
'''
# 1 - Phương Thức Seek 
'''         Cú pháp : <File>.seek(offset, whence=0)
        Một text file sẽ chỉ được sử dụng whence = 0. whence = 1 hoặc whence = 2 chỉ sử dụng với binary file.
        Do đó, ta cũng không cần quan tâm tới parameter whence.
=>  Phương thức này giúp ta di chuyển con trỏ từ vị trí đầu file qua offset kí tự. Và 
        parameter offset phải là một số tự nhiên.
     + Nhờ phương thức này, ta có thể ghi nội dung từ bất cứ đâu trong file.
     + Và từ đó ta có thể đọc lại file sau khi ta đưa con trỏ file xuống cuối file.
'''
# Mở file để đọc 
file_object4=open('file1.txt')
# Đọc file với read()
data4=file_object4.read()   
print(data4,'\n')       
# Hiện tại con trỏ file đang ở cuối file và ta ko thể đọc lại file này nữa 

# Di chuyển con trỏ file lên vị trí đầu tiền của file 
file_object4.seek(0)
print(file_object4.read(),'\n')

# Di chuyển con trỏ file lên vị trí thứ 5 của file 
file_object4.seek(5)
print(file_object4.read(),'\n')

file_object4.close()

'''             VI- Câu Lệnh With 
        Cấu trúc cơ bản của câu lệnh with :
            with expression [as variable]:
                with-block    
        Chú ý rằng : with-block nằm thụt vào so với dòng with expression
        Đặc điểm của with khi sử dụng với file là : khi kết thúc with-block thì File sẽ được đóng 
'''
with open('file1.txt') as file_object5:
    data5=file_object5.read()
print(data5)
# Ở đây file đã đóng nên ta ko thể thao tác bất cứ j trên file này nữa 
