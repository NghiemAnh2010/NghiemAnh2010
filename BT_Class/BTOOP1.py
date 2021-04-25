'''    Viết chương trình quản lý công đoàn , người dùng nhập vào tên CD ,tên ca sỹ, số bài hát 
    giá thành 
'''
class Cong_Doan:
    def __init__(self,nameCdIN,nameCasyIN,numBaihatIN,priceIN):
        self.name_CD=nameCdIN
        self.name_CaSy=nameCasyIN
        self.num_Baihat=numBaihatIN
        self.price=priceIN
    def __str__(self):
        return "# {} - {} - {} - {}".format(self.name_CD,self.name_CaSy,self.num_Baihat,self.price)
choice=1
DSCD=[]
while choice == 1:
    print('--------Danh sach CD :--------')
    print('Nhap thong tin CD :')
    name_CDIN=str(input('Nhap ten CD:'))
    name_CaSyIN=str(input('Nhap ten ca sy:'))
    num_BaihatIN=int(input('Nhap so bai hat:'))
    priceIN=float(input('Nhap gia tien:'))
    cd=Cong_Doan(name_CDIN,name_CaSyIN,num_BaihatIN,priceIN)
    DSCD.append(cd)
    print('Tiep tuc nhap : 1:Có , 0:Không')
    choice=int(input())
tong_Tien=0
for cd in DSCD:
    print(cd)
    tong_Tien+=cd.price
print('Tong gia thanh:',tong_Tien)