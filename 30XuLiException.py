'''
    I - Xử lí ngoại lệ bằng khối lệnh try: ... except:
- Phần thân của try bao gồm các dòng code có thể tạo ra các exception
    nếu 1 exception được tạo ra thì tất cả các câu lệnh trong khối sẽ bị bỏ qua 
- Phần thân của except: được gọi là exception handling được dùng để bắt lỗi exception 

'''
'''
    II- Xử lí cụ thể 1 ngoại lệ:
ở phần xử lí ngoại lệ trên thì ko có 1 ngoại lệ cụ thể nào được đề cập đến trong mệnh đề except 
cả nên khi chương trình gặp ngoại lệ thì dù bất cứ ngoại lệ nào cx được xử lí chung theo 1 cách

    Cú pháp : try:
                    # code
              except exceptionName:
                    # code
    Với exceptionName là tên của các exception mà bạn nghĩ có thể xảy ra
    + 1 mệnh đề try có thể có nhiều mệnh đề except 
'''
'''
try:
    m=int(input('Nhap 1 so chia'))
    num2=10
    def check():
        num1=10
    print(num1)
    n=num2//m
except NameError:
    print('Bien cua ban ko duoc xac dinh ')
except ZeroDivisionError:
    print('Vui long nhap 1 so chia khac 0')
except ValueError:
    print('Dinh dang dau vao ko hop le!!!')
'''
'''
    III-    Xây dựng 1 Exception :
        Xây dựng exception bằng cách sử dụng raise là 1 cách khác để xử lí ngoại lệ trong Python
    TH này bạn có thể tạo ra exception cho riêng mk , đó là exception được nêu ra khi vấn đề nằm bên
     ngoài phạm vi dự kiến của lỗi xảy ra
'''
try: 
    x=int(input('Nhap 1 so trong khoang tu 1 den 10 :'))
    if x<1 or x>10:
        raise Exception
    print ('Ban vua nhap 1 so hop le!')

except ValueError:
    print('Dinh dang dau vao ko hop le')
except:
    print('So ban nhap nam ngoai khoang cho phep!!!')

'''
    IV- Module traceback
        Nó sử dụng để in ra dấu vết của chương trình sau khi exception xảy ra
    Traceback bào gồm thông báo lỗi , số dòng gây ra lỗi và call stack của hàm gây ra lỗi
'''
'''
    V - Try .... Finally
        Finally còn được gọi là mệnh đề clean-up/termination vì nó luôn luôn chạy bất kể có lỗi nào xảy ra
        trong block try
'''