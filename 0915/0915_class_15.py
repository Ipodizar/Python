# 깃에서 14번 다운 받아서 비교하기
# 클래스
# 클래스 변수, 인스턴스 변수
# 생성자 __inti__
# 메소드 __str__ __eq__ __ne__ __lt__ __gt__ __le__ __ge__
# property : getter, setter, deleter, private --> 함수를 변수처럼 사용할 때
# 객체생성

# 상품 클래스명  Product
# 상품명 product_name, 가격 product_price, 재고 product_stock

class Product:
    count = 0
    def __init__ (self, product_name, product_price, product_stock):
        self.id = Product.count + 1
        Product.count += 1
        self._product_name = product_name
        self._product_price = product_price
        self._product_stock = product_stock

    @property
    def product_name(self):
        return self._product_name

    @property
    def product_price(self):
        return self._product_price 

    @property
    def product_stock(self):
        return self._product_stock 
    
    @product_name.setter
    def product_name(self, name):
        self._product_name = name

    @product_price.setter
    def product_price(self, price):
        if price < 0:
            print("0보다 작은 값은 입력할 수 없습니다.")
        else:
            self._product_price = price

    @product_stock.setter
    def product_stock(self, stock):
        self._product_stock = stock

    def __str__(self):
        return f'상품명 : {self._product_name}, \
        가격 : {self._product_price}, 재고 : {self._product_stock}'
    
    def __eq__(self, value):
        return self._product_stock == value._product_stock
    
products = [
    Product("노트북", 30000000, 10),   # Product 클래스로 만든 객체들
    Product("스마트폰", 16000000, 20),
    Product("태블릿", 12000000, 30)
]

    # 노트북의 가격을 20% 할인
products[0].product_price *= 0.8
# for p in products:
#     if print(p).product_name == '노트북':
#           p.product_price = p.product_price * 0.8

    # 스마트폰의 가격을 10% 인상
products[1].product_price *= 1.1
# for p in products:
#     if print(p).product_name == '스마트폰':
#           p.product_price = p.product_price * 1.1

    # 전체제품 출력
for i in products:
    print(i)

    # 제품 추가
products.append(("에어팟", 300000, 0))

    # 제품 삭제 - 수량이 남아 있으면 삭제 못 하게
del products[3]
for i in products:
    print(i)

# 현재 모든 제품의 수량의 합
# all_product_stock = 0
# for i in products:
#      all_product_stock += products[i].product_stock
# print(all_product_stock)

total_stock = 0
for p in products:
    total_stock += p.product_stock

print(total_stock)

    # 가격 * 수량을 기준으로 같다 크다 크거나 같다 작다 작거나 같다

  


