'''
    I - Module chỉ đơn giản là những file Python  , là cách mà chúng ta phân hóa chương trình thành các nhánh nhỏ
        cho dễ quản lý và gọi lại chúng khi nào ta cần . Như vậy chương trình của chúng ta sẽ có tính tái sử dụng 
        và baỏ trì cao
    + Chú ý : các module phải được tạo cùng thứ mục
'''

#   II - Câu lệnh Import
import a

a.say('NghiemAnh')

#   III- Câu lệnh from import
'''         Trong TH nào đó bạn ko muốn sử dụng hết toàn bộ module mà chỉ muốn sử dụng 1 số thứ trong đó thôi
    thi ta dùng từ khóa from...import
'''
list1=[1,2,3,4,5]
from a import func_N        # Ta ko còn phải sử dụng module object nữa
print(func_N(list1))

'''     Khi ta muốn import nhiều hơn 1 attribute hay method thì ta sử dụng thêm các dấu ,
    VD : from a import fun_N,bye
'''

#   IV - Import 1 module nhiều lần 
'''     
    + Sử dụng import hay from import để import một module thì chỉ hoạt động một lần

'''
import py
print(py.new_V)
py.new_V=100

import py
print(py.new_V)

# => Ta thấy rằng Hello chỉ hiện ra 1 lần mặc dù ta gõ tới 2 dòng lệnh import py ,và biến new_V của chúng ta 
#       cũng ko bị reset trở lại 10

#   1- Khi sử dụng from...import rồi sau đó sử dụng import thì import lần 2 được coi như là 1 cách reset trờ lại 

#  V - Reload module 
'''     Python chỉ cho phép ta import 1 lần ,ko tự động reload , ko có nghĩa là chúng ta ko thể reload lại module 
    . Ta có thể sử dụng hàm reload trong thư viện của Python 
'''

