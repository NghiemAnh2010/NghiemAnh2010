'''
I - Error : 
    1- Lỗi cú pháp do ko tuân thủ theo đúng cú pháp ( syntax error or parsing error)
        Hoặc invalid syntax
II -Exception ( Ngoại lệ):
    Những lỗi phát sinh khi thực thi chương trình (runtime error) được gọi là các ngoại lệ
 1-Mở 1 tệp ko tồn tại (FileNotFoundError)
 2-Chia 1 số cho 0 (ZeroDivisionError)
 3-KO tìm thấy module được import (ImportError)
 4-Truyền giá trị vào 1 function với đúng kiểu dữ liệu nhưng giá trị ko thích hợp (ValueError)

 * Có rất nhiều ngoại lệ được tạo ra kh gặp các lỗi tương ứng 
 Ta có thể xem tất cả các TH Exception có sẵn bằng cách sử dụng hàm local() như sau :
 local()['__builtins__']

'''
locals()['__builtins__']