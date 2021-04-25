'''
    Yêu cầu: Xây dựng ứng dụng quản lý danh sách các giao dịch:Mô tả:Hệ thống quản lý 2
loại giao dịch:
1-Giao dịch vàng: Mã giao dịch, ngày giao dịch (ngày/tháng/năm), đơn giá, số lượng, loại
vàngcó 3 loại 18k, 24k, 9999.
2-Giao dịch tiền tệ: Mã giao dịch, ngày giao dịch (ngày/tháng/năm), tỷ giá (cũng là đơn giá),
số lượng, loại tiền tệ có 3 loại:USD, EUR, AUD, loại giao dịch mua/bán. Thành tiền được
    Nếu loại giao dịch là “mua”thì: thành tiền = số lượng * tỷ giá
    Nếu loại giao dịch là “bán” thì: thành tiền = (số lượng * tỷ giá)* 1.05
'''
from BTOOP2Gold import *
from BTOOP2Money import *

def typeGD(x):
    switcher={
        1:'Chon loai GD : 18k / 24k / 9999:',
        2:'Chon loai GD : USD / EUR / AUD :'
    }
    return switcher.get(x,'nothing')

def __main__():
    print('Quan ly giao dich')
    DSGD=[]
    choice=1
    while choice==1:
        code_GDIN= str(input('Nhap ma giao dich:'))
        date_GDIN= str(input('Nhap ngay GD:'))
        num_GDIN= int(input('Nhap so luong GD:'))
        x=int(input('Chon loai GD : 1-Vang , 2- Tien te :'))
        print(typeGD(x))
        type_GDIN=str(input())
        price_GDIN=float(input('Nhap don gia :'))
        if x==1:
            GD1=GDGold(code_GDIN,date_GDIN,num_GDIN,price_GDIN,type_GDIN)
            DSGD.append(GD1)
        elif x==2:
            actionIN=int(input('Ban mua hay ban ? 1:Mua, 2:Bán :'))
            GD1=GDMoney(code_GDIN, date_GDIN, num_GDIN, price_GDIN, type_GDIN,actionIN)
            DSGD.append(GD1)
        choice=int(input('Ban co muon tiep tuc giao dich ? 1:Có , 0:Không :'))
    sum_PriceGD=0
    for GD in DSGD:
        print(GD)
        sum_PriceGD+=GD.sumPrice1()
    print('Tong gia tri giao dich la :',sum_PriceGD)
if __name__ =="__main__":
    __main__()
