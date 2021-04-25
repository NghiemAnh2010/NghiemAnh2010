
from BTOOP2GD import *
class GDGold(GiaoDich):
    def __init__(self,code_GDIN,date_GDIN,num_GDIN,price_GDIN,type_GDIN):
        self.code_GD=code_GDIN
        self.date_GD=date_GDIN
        self.num_GD=num_GDIN
        self.price_GD=price_GDIN
        self.type_GD=type_GDIN
    def sumPrice1(self):
        return self.num_GD*self.price_GD
    def __str__(self):
        return "{} - {} - {} - {} - {} - 'Thanh tien ='{}".format(self.code_GD,self.date_GD,self.type_GD,self.num_GD,self.price_GD,self.sumPrice1())
