'''                         
                            KIỂU DỮ LIỆU DICT TRONG PYTHON
1- Dict(Dictionary) cũng là 1 container như List , Tuple hay Set . Khác là List , Tuple có cac indexing để phân
    biệt các phần tử còn Dict lại dùng các key để phân biệt 
Một Dict gồm các yếu tố sau:
    + Được giới hạn bởi cặp ngoặc nhọn {}, tất cả những gì nằm trong đó là những phần tử của Dict
    + Các phần tử của Dict được phân cách nhau ra bởi dấu phẩy (,).
    + Các phần tử của Dict phải là một cặp key-value
    + Cặp key-value của phần tử trong Dict được phân cách bởi dấu hai chấm (:)
    + Các key buộc phải là một hash object 
2- Khởi tạo Dict :
    Cú pháp : {<key_1: value_1>, <key_2: value_2>, .., <key_n: value_n>}
'''
dic1={'name':'QuangAnh' , 'age': 20}
print(dic1,'\n')
print(type(dic1),'\n')

# Khởi tạo 1 dict rỗng :empty dict
empty_dic={}
print(empty_dic,'\n')
print(type(empty_dic),'\n')

# 3- Sử dụng Dict Comprehension 
dic2 ={key : value for key , value in [('name','QuangAnh'),('age',20)] }
print(dic2,'\n')

# 4 - Sử dụng Contructor Dict
''' Với Dict ta có 4 cách để khởi tạo 1 Dict bằng contructor
'''
# 4_1 : Khởi tạo 1 dict rỗng 
dic3=dict()
print(dic3,'\n')

# 4_2 : Khởi tạo 1 dict từ 1 mapping object : Cú pháp : dict(mapping)
''' Trong đó mapping object cũng gần giống so với dict object 
        + Một object là mapping khi có đủ 2 phương thức keys và __getitem__ 
        + Dict object cũng là 1 mapping object .Tuy nhiền ko phải mapping object nào cũng là dict object 
            vì dict object không chỉ có 2 phương thức trên mà còn nhiều phương thức khác 
'''
'''
class Map_Class :
        def keys(self):
            return [1,2,3]
        def __getitem__(self,key):
            return key*2
map_obj=Map_Class
dic4 =dict(self,map_obj)
print(dic4)
'''

# 4_3 :Khởi tạo bằng iterable : Cú pháp : dict(iterable)
'''         Trong đó iterable này đặc biệt hơn các iterable mà ta dùng ở List , Tuple đó là các phần tử trong 
    iterable pải có 2 value đó chính là cặp key_value
            Ta có thể dùng list ,tuple hoặc bất cứ container nào trừ mapping object để chứa cặp <key:value>
'''
lst1=[('one',1),('two',2),('three',3),('four',4)]
dic5=dict(lst1)
print(dic5,'\n')
c1=(('name','qanh'),('age','20'))
dic6=dict(c1)
print(dic6,'\n')

# 4_4 : Khởi tạo bằng keyword arguments     : Cú pháp : dict(**kwargs)
'''     Trong đó leyword argument là đối số bạn truyền vào cho hàm
            + Đơn giản là bạn khởi tạo 1 biến và giá trị rồi đưa biến đó cho dict giữ hộ
            + Lưu ý rằng , biến này không bị ảnh hưởng hoặc ảnh hưởng gì tới các biến bên ngoài 
'''
name = 'QuangAnh'
Id1 =2010
dic7=dict(name='Hello' , Id1= 2001)         # name và Id1 ở đây là biến cục bộ
print(dic7,'\n')

print(name,'\n')


# 4_5 Sử dụng phương thức fromkeys  : Cú pháp : dict.fromkeys(iterable,value)
'''         Cách này cho phép ta khởi tạo 1 dict với các keys nằm trong 1 iterable .
            Các giá trị này đều sẽ nhận 1 giá trị mặc định là None 
'''
iter1=('name','age')
dic8=dict.fromkeys(iter1,'quanganh')
print(dic8,'\n')

'''     IV- Lấy Value trong Dict bằng key 
            Cú pháp : Your_dict[key]
'''
print(dic7,'\n')
print(dic7['Id1'],'\n')
print(dic7['name'],'\n')

'''     V-Thay đổi nội dung Dict trong Python
Vì dict là 1 unhashable object nên ta có thay đổi nội dung trong dict 1 cách trực tiếp 
'''
print(dic7,'\n')
dic7['name']='Quang Anh'
dic7['Id1']= dic7['Id1'] + 20
print(dic7,'\n')

'''     VI -Thêm thủ công 1 phần tử vào Dict
    Cách này giống với việc bạn thay đổi nội dung của Dict .Khác ở chỗ bây giờ bạn sử dụng 1 key chưa hề có trong Dict
'''
print(dic7,'\n')
dic7['Age'] = 20
print(dic7,'\n')