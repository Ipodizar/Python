# 실행결과 이상함. 확인 필요

class People():
    # 생성자 : 객체 생성 시 함수 자동 생성
    def __init__(self): # self 무조건 있어야한단다
        self.name = None
        self.age = None
        self.addr = None
        print('생성자 호출')

print('h1 객체 생성 전')
h1 = People()
print('h1 객체 생성 후')
# h1.make_instance() # self == h1, 이게 실행되었기 때문에 h1의 name, age, addr 생긴거임
print(h1.addr)
h2 = People()
# h2.make_instance()
print(h2.addr)