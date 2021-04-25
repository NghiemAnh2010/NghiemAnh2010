'''
    1-Sự khác nhau giữa '' và "": Về công dụng thì nó là như nhau , những thứ nằm bên trong nó là 1 chuỗi 
    2- Chuỗi nhiều dòng với '" và """ 
    3- Sự so sánh giữa các chuỗi được thực hiện dựa trên giá trị ASCII.
'''

# Một chuỗi bên trong có chứa '
s="I'm beginer"
print(s,'\n')

# Chuỗi nhiều dòng với ''' và """

s1='''      Dong 1
       Dong 2
       Dong 3'''
print(s1,'\n')

# Chuỗi vừa có ký tự ' và "
s3=""" I'm beginer " Good luck"""
print(s3)
print(s3[6:])
#   Escape Sequence : là 1 chuỗi đặc biệt trong python bắt đầu với 1 dấu \
'''     \a: phát ra 1 tiếng bíp
        \b : Backspace
        \' : In ra kí tự '
        \\ : IN ra kí tự \
        \n : newline 
        \s : space 
        \t : tab 
'''