'''     
    I-Các Phương Thức Tiện Ich
'''
# 1-Phương Thức Copy()
'''         Cú pháp : <Dict>.copy()
            Trả về 1 bản sao của dict
'''
dct1={'name':'quanganh','age':20,(1,2):2010}
dct2=dct1.copy()
print(dct2,'\n')

# 2-Phương Thức clear()
'''         Cú pháp : <Dict>.clear()
            Loại bỏ tất cả các phần tử trong dict
'''

'''     II-CÁC PHƯƠNG THỨC XỬ LÍ
'''
# 1- Phương thức Get
'''         Cú pháp : <Dict>.get(key [,default])
            Trả về giá trị của khóa key.Nếu key ko có trong Dict thì trả về giá trị default 
            Default có giá trị mặc định là None nếu chúng ta ko truyền vào
'''
k1=dct1.get('name')
print(k1,'\n')

# Với key ko nằm trong Dict và default là mặc định
k2=dct1.get('a')
print(k2,'\n')
# Với key ko nằm trong Dict và default được truyền vào
k3=dct1.get('b','Hello')
print(k3,'\n')

# 2- Phương thức items()
'''         Cú pháp : <Dict>.items()
            Trả về 1 giá trị thuộc lớp dict_items .Các giá trị của dict_items sẽ là 1 tuple với 
                giá trị thứ 1 là key , giá trị thứ 2 là value
            Dict_items là 1 iterable 
'''
item1=dct1.items()
print(item1,'\n')
# Vì dict_items là 1 iterable nên ta có thể sử dụng các contructor của các kiểu dữ liệu để khởi tạo kiểu dữ liệu đó

lst1=list(item1)
print(lst1,'\n')

# 3-Phương Thức Keys 
'''         Cú pháp :<Dict>.keys()
            Trả về 1 giá trị thuộc lớp dict_keys. Các giá trị của dict_keys sẽ là các key trong Dict
            Dict_keys là 1 iterable
'''
key1=dct1.keys()
print(key1,'\n')
# Dict_keys là 1 iterable nên ta có thể dùng được contructor
tup1=tuple(key1)
print(tup1,'\n')

# 4-Phương Thức Values
'''         Cú pháp :<Dict>.values()
            Trả về 1 giá trị thuộc lớp Dict_values .Các giá trị của dict_values sẽ là các value trong Dict
             Dict_value cũng là 1 iterabel
'''
value1=dct1.values()
print(value1,'\n') 

# 5- Phương thức pop():
'''         Cú pháp : <Dict>.pop(key,[default])
            Bỏ đi phần tử key và trả về giá trị value của phần tử key đó 
            Nếu key ko có trong Dict : + Báo lỗi keyerror nếu default là None
                                       + Trả về defalut nếu ta thêm default vào
'''
print(dct1,'\n')
p1=dct1.pop('name')
print(p1,'\n') 
print(dct1,'\n')

dct3={'name':'NBQA','age':20,('a','b'):('a','b')}
print(dct3,'\n')
# TH key ko có trong dict và default là mặc đinh SẼ CÓ LỖI
# TH key ko có trong dict và default = 'Hello 
p2=dct3.pop('key','Hello')     
print(p2,'\n')

# 6-Phương Thức popitem
'''         Cú pháp : <Dict>.popitem()
            Trả về Trả về một 2-tuple với key và value tương ứng bất kì (vấn đề này liên quan đến giá trị 
                của hash của key
            Do đó bạn cũng hiểu vì sao key buộc phải là một hash object) trong Dict.
             Và cặp key-value sẽ bị loại bỏ ra khỏi Dict.
'''
dct4={'name':'NBQA','age':20,('a','b'):('a','b')}
tup2=dct4.popitem()
print(tup2,'\n')

#   7 - Phương thức setdefault
'''             Cú pháp : <Dict>.setdefault(key [,default])
                Trả về giá trị của key trong Dict 
                Nếu key ko có trong Dict thì sẽ trả về giá trj default 
                và tự động thêm key ko có đó vào Dict với value của key đó là default
'''
dct5={'name':'NBQA','age':20,('a','b'):(1,2)}
set1=dct5.setdefault('name')            # TH key có trong dict
print(set1,'\n')
print(dct5,'\n')
# TH key không có trong Dict và default khác None 
set2=dct5.setdefault('address','HungYen')
print(set2,'\n')
print(dct5,'\n')

# 8-Phương Thức Update():
'''         Cú pháp :<D>.update([E, ]**F)
            Phương thức giúp bạn cập nhật nội dung cho Dict.
            1-F là một Dict được tạo thành bởi packing arguments 
                Và sẽ thêm vào Dict bằng cách:
                    for k in F: D[k] = F[k]
            2-Nếu E được truyền vào và đối tượng E có phương thức keys(), thì  sẽ cập nhật Dict bằng cách:
                    for k in E: D[k] = E[k]
            3-Nếu E được truyền vào và đối tượng E, 
                đối tượng này có các giá trị là một container chứa hai giá trị thì sẽ cập nhật Dict bằng cách.
                for k, v in E: D[k] = v
'''
# Update theo kiểu packing arguments
dct6={'name':'NBQA','age':20}
print(dct6,'\n')
dct6.update(address1='HungYen',Id1=2010)        # Với address1 và Id1 là các biến 
print(dct6,'\n')

# Update với cách bạn truyền E với E là 1 đối tượng có phương thức keys
dct7={'name':'quanganh'}
E={'age':20,'Id':2010}
print(dct7,'\n')
dct7.update(E)
print(dct7,'\n')

# Update với truyền vào 1 E vơi E có các giá trị là 1 container chứa 2 giá trị
dct8={'name':'quanganh'}
E1=[('age',20),('address','HungYen')]
print(dct8,'\n')
dct8.update(E1)
print(dct8,'\n')

