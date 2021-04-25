''' 
1- Chuỗi Trần :  Chuỗi này sẽ không quan tâm đến thứ gọi là Escape Sequence
            Cú pháp : r'<Nội dung chuỗi>'
'''
# Nội dung chuỗi trần được gán vào biến s
s= r'\neu mot ngay'
print(s)

'''
II-  Một số toán tử với chuỗi
    1- Toán tử +
        Dùng để nối 2 chuỗi với nhau : A+B 
    2-Toán tử * :
        Toán tử này giúp ta tạo ra 1 chuỗi nhờ lặp đi lặp lại chuỗi với số lân bạn muốn
        Cú pháp : A*N (Với A là 1 chuỗi và N là số lần lap lại của chuỗi A)
    3-Toán tử in :
        Toán tử này bản chỉ có thể nhận 1 trong 3 đáp án đó la True hoặc False
        Cú pháp : s in A ( Vói s và A là chuỗi )
        Kết quả là True nếu xuất hiện chuỗi s trong A , và ngược lại
    4- Toán tử Indexing và cắt chuỗi :
        +Lấy bất kỳ kí tự nào có trong chuỗi bằng cú pháp : <Tên chuỗi>[<Vị trí của kí tự đó trong chuỗi>]
        +Chuỗi không chỉ đánh dấu vị trí của các phần tư bên trong chuỗi từ 0->n-1 mà còn đánh dấu vị trí từ -n -> -1
        + Ta có thể dùng hàm len(<tên chuỗi>) : để tìm được só lượng các kí tự có trong 1 chuỗi 

        4_2 : Cắt Chuỗi:
            Cú pháp: <Tên chuỗi>[Vị trí bắt đầu : Vị tris dừng]
            Khi ta ử dụng chuỗi này ta sẽ nhận được 1 chuỗi  Chuỗi này chính là bản sao của chuỗi mà chúng ta muốn
                cắt . Ta lấy nó từ vị trí <Vị trí bắt đầu> đến < Vị trí dừng > - 1
'''
# Nối chuỗi với toán tử +
s1="Hello "
s2="Quang Anh"
s3=s1+s2
print(s3,'\n')

#Lũy thừa chuỗi với *
s4=s1*3
print(s4,'\n')

# Toán tử in:
print(s1 in s2)
print(s1 in s3)

# Toán tử Index : lấy ra 1 kí tự trong chuỗi
print(s3[2],'\n')

# Cắt chuỗi :
'''     Cú pháp : <Chuỗi> [vị trí bắt đầu : ví trí dừng] 
        Khi sử dụng cú pháp này ta sẽ nhận được 1 chuỗi gồm các kí tự từ <vị trí bắt đầu> đến <vị trí dung> - 1
        Cú pháp 2: <Chuỗi> [<Vị trí bắt đầu>:<Bước nhảy>:<Vị trí dừng>]
'''
s5=s3[5:11]
print(s5,'\n')          # Cắt chuỗi s3 từ vị trí 5 đến 10
print(s3[-15:-6],"\n")  # Cắt chuỗi s3 từ vị trí -15 đến -6
print(s3[5:],'\n')      # Cắt chuỗi s3 từ vi trí 5 đến tất cả các vị trí còn lại sau vtri 5

''' 5-Ép Kiểu Dữ liệu :
    cú pháp : <Tên kiểu dữ liệu>(<Tên biến>)
'''

''' 6- Thay đổi nội dung của chuỗi:
+ Nếu bạn muốn thay đổi nội dung của chuỗi nhờ Indexing ở các ngôn ngữ khác thì được nhưng ở Python thì không cho
    phép bạn làm điều đó
+ Bạn phải thay đổi chuỗi 1 cách gián tiếp bằng việc dùng toán tử + để nối 1 chuỗi với 1 chuỗi mới cần thay đổi
'''
a="abc xyz"
print(a,'\n')
# a[0]="A"   # Sẽ xảy ra lỗi ở đây vì python không cho phép bạn làm vậy

# Muốn thay kí tự ở vị trí đầu tiên của chuỗi a thì ta làm như sau
a= 'F' + a[1:]
print(a,'\n')

# Vì ta không thể thay thế nội dung của chuỗi do đó kiểu dữ liệu chuỗi là 1 đối tượng có thể băm 
# Vì nó là 1 hashable object nên ta có thể sử dụng hàm hash : Đối tượng không được động vào 
print(hash(a))