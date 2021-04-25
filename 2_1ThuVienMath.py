''' 
        Để sử dụng 1 thư viện nào đó ta dùng lệnh:
            import.<Tên thư viện>
        Muốn sử dụng hàm nào đó của thư viện ta sử dụng cú phấp 
            <Tên thư viện>.<tên hàm>

        Một số hàm thường dùng trong tính toán :
            .trunc(x) : Trả về số nguyên là phần nguyên của số x
            .floor(x) : Trả về 1 số nguyên được làm tròn từ số x , kết quả luôn <= x
            .ceil(x)  : Trả về 1 số nguyên được làm tròn từ ố x , kết quả luôn >= x
            .fabs(x)  : Trả về 1 số thực là trị tuyệt đối của số x 
            .sqrt(x)  : Trả về 1 số thực là căn bậc 2 cảu số x
            .gcd(x,y) : Trả về 1 số nguyên là ước chung lớn nhất của 2 số x và y

'''
import math
print(math.trunc(3.34),'\n')
print(math.floor(4.98),'\n')
