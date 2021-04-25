'''
    Đây là 1 abstract class là 1 class mà bên trong nó chứa 1 hoặc nhiều phương thức trừu tượng
'''
from abc import ABC,abstractmethod

class GiaoDich(ABC):
    # Khai báo phương thức trừu tượng 
    @abstractmethod
    def __init__(self,code_GDIN,date_GDIN,num_GDIN,price_GDIN,type_GDIN):
        pass
    @abstractmethod
    def sumPrice1(self):
        pass
    @abstractmethod
    def __str__(self):
        pass