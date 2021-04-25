'''
    I-      Gioi Thiệu Lại về Iterables 
        Mọi thứ mà bạn có thể dùng cú pháp '' for ... in .." đều là 1 iterable .
        VD như List, Chuỗi , Tuple , File ,...
        Những iterable này rất thuận tiện cho chúng ta truy xuất thông tin trong nó , muốn làm được vậy bạn phải 
            lưu trữ nó trong vùng nhớ của máy tính .Vì lẽ đó sẽ có trường hợp bạn ko cần thiết pải giữ tất cả 
            các thông tin cùng 1 lúc vì nó quá nhiều 
'''

''' 
    II -  Gioi Thiệu Về Generator 
        Generator là iterator , 1 dạng của iterable nhưng khác ở chỗ bạn ko thể tái sự dụng .
        Vì generator ko lưu trữ tất cả các phần tử của bạn trong bộ nhớ , mà nó sinh ra lần lượt
'''
gen_1=(x for x in range(5))
print(type(gen_1))
# Ko thể xuất toàn bộ 1 generator bằng hàm print 1 lúc mà phải dùng for để xuất từng phần tử 
for i in gen_1:
    print(i)
# KO thể tái sử dụng generator khi nó đã được xuất ra  
'''     Vì khi in ra giá trị đầu tiên là 0, khi bạn kêu nó sinh tiếp ra giá trị 1 , nó sẽ vứt bỏ giá trị 0 đi 
    để nhường chỗ cho giá trị 1 ,nó tiếp tục làm như vậy đến khi kết thúc 
'''
for i in gen_1:
    print(i)

#      III- Lệnh Yield (Năng suất)
'''  Lệnh Yield có cách sử dụng gần giống với lệnh return 
     Khác với lệnh return ở chỗ là Return trả về 1 object thì Yield trả về 1 generator 
'''
def scare (lst1):
    s_lst=[]
    for i in lst1:
        s_lst.append(i**2)
    return s_lst
lst2=[1,2,3]
s_lst=scare(lst2)
print(s_lst)

def scare1(lst):
    for i in lst:
        yield i**2
new_lst=scare(lst2)
# Vì lệnh Yield trả về 1 generator nên phải dùng for để xuất từng giá trị 1
for i in new_lst:
    print(i)
''' => Hàm return sẽ quăng ra toàn bộ giá trị sau khi bình phương nên ta pải tạo 1 list để lưu giữ nó còn 
    với Yield thì nó sẽ lần lượt sinh ra từng giá trị sau khi bình phương mà ko cần 1 list để lưu trữ 
    + Khi dùng Yield , những dòng lệnh trong hàm ko chạy ngay mà nó trả về 1 generator , mỗi khi bạn yêu cầu nó 
        sinh nó mới bắt đầu chạy vào bên trong thực hiện nhũng dòng lệnh cho hàm cho đến khi gặp lệnh Yield thì 
        nó sẽ sinh ra giá trị bạn yêu cầu Yield , hàm bây giờ được tạm dừng , nếu lần sau gọi lại nó sẽ chạy tiếp 
        tục ở phần đó chứ ko pải chạy lại từ đầu 
'''
def genZ():
    yield 'Qanh'
    print('This is the second yield ')
    yield 'NBQA'
    print('This is the last yield')
    yield 20
    print('Congturation')
for i in genZ():
    print(i)
# ===> Ko giống như hàm return sẽ kết thúc hàm , với lệnh yield thì hàm vẫn sẽ được tiếp tục thực hiện 
# Ngoài cách dùng for để duyệt Generator thì ta có thể dùng next để duyệt chúng

#       IV- Phương thức send 
'''    Đây là phương thức giúp ta gửi giá trị vào trong 1 generator 
        Cú pháp : generator.send(value)
'''
def gen():
    for i in range(4):
        x= yield i
        print('value sent from you ',x)
g=gen()  # gán generator này cho biến g
print(next(g))
g.send('HELLO')     # Ta gửi giá trị 'HELLO' vào trong generator với i=1 
g.send('Qanh')
# Lần này ta ko dùng send nên mặc định giá trị gửi vào là None
print(next(g))

# ===> Tốc độ xử lí của generator sẽ nhanh hơn rất nhiều so với việc sử dung iterable lưu tất cả các phần từ vào 
