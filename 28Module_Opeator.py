'''
    Operator là 1 module tích hợp cung cấp 1 tập hợp các toán tử thuận tiện .

    Trong operator.itemgetter(n) xấy 1 dựng 1 hàm có thể gọi được , giẳ sử 1 đối tượng có thể lặp 
lại (VD: list,tuple,set) làm đầu vào và lấy phần tử thứ n ra khỏi nó
    Vì vậy bạn ko thể sử dụng key=[x][1] vì x ở đây ko hiểu là gì 
    Thay vào đó bạn có thể sử dụng key=lambda emel : emel[1] với emel là 1 container nào đó

** Để sắp xếp nhiều hơn 1 cột ta sử dụng có thể truyền nhiều giá trị cho key thông qua tuple ..
Hoặc có thể sử dụng itemgetter với nhiều chỉ mục :
    operator.itemgetter(1,2) hoặc với :lambda :emel :(emel[1],emel[2])
'''
