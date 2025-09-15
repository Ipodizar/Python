# 생성자 : 객체 생성 시 함수 자동 생성
class Product():
    serial_num = 0
    def __init__(self): # self 무조건 있어야한단다
        Product.serial_num += 1
        self.serial_num = Product.serial_num
        self.name = None
        
tv1 = Product()
tv2 = Product()
tv3 = Product()
print(tv1.serial_num, tv2.serial_num, tv3.serial_num)