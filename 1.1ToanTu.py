# 1- Toán tử số học :
'''
    // : Chia lấy phần nguyên , xóa đi các chữ số sau dấu phẩy 
    % : Chia lấy dư 
    **: phép lấy số mũ 
# 2- Toán tử quan hệ :
    != : ko bằng
    <> : không bằng 
    ==: bằng
# 3 - Toán tử gán :
    /= : chia toán hạng trái cho toán hạng phải rồi gán giá trị đó cho toán hạng trái
    //=  : thực hiện phép chia // và gán 
    %= : chia lấy phần dư và gán
# 4- Toán tử logic :
    and : phép và , kết quả sẽ trả về True nếu cả 2 đk là true 
    or :
    not : phép phủ định để đảo ngược trạng thái logic của toán hạng
# 5- Toán tử membership :
    in : trả về true nếu 1 biến nằm trong dãy các biến 
    not in: ngược lại với in 
# 6- Toán tử identify:
    is : Trả về true nếu các biến ở 2 bên toán tử cùng trỏ tới 1 đối tượng 
    not is : ngược lại với is
# 7- Toán tử thao tác bit :
'''
n= 8
m= 3
# Toán tử số học:
print(n//m)     # 2
print(n/m)      # 2
print(n**m)     # 8^3

# Toán tử quan hệ:
print(n!=m)     # True
print(n==m)     # False


# Toán tử identiffy
n1=8
id1= id(12)
id2= id(12)
print(id1)
print(id2)
print(n is n1)          # True
print(id1 is id2)       # False

# Toán tử membership:
lst1=[1,2,3,4,5]
print(2 in lst1)        # True
