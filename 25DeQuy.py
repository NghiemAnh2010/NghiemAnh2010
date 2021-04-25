'''
    I - Đệ quy : là cách chia nhỏ bài toán thành các bài toán nhỏ hơn và đơn giản hơn mà máy tính của bạn
        có thể xử lí được 
'''
# Minh họa đệ quy bằng việc tính tổng của 1 list

def sum1(lst):
    if not lst:
        return 0
    else :
        return lst[0]+sum1(lst[1:])
lst1=[1,2,3,4,5,6,7,8,9]
result = sum1(lst1)
print(result)

#       II -Đệ quy theo cách python 
'''   Ta sử dụng if/else trong lambda hay còn gọi là ternary expression
'''
def sum2(lst):
    return 0 if len(lst)==0 else lst[0]+sum2(lst[1:])
print(sum2(lst1))

# Ta cũng có thể  sủ dụng paking argument
# Đệ quy cũng có thể chuyển hướng 
def sum3(lst):
    return 0 if not lst else sum4(lst)
def sum4(lst):
    return lst[0]+sum3(lst[1:])
    