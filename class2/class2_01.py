# 상속의 정의
# 상속은 기존 클래스의 속성과 메서드를 새로운 클래스가 물려받는 것
# 상속을 통해 코드의 재사용성을 높이고, 계층적인 관계를 표현
# 상속의 기본 문법
# class 부모클래스:
#   def 부모메서드(self):
#       print("부모 메서드 호출")

# class 자식클래스(부모클래스):
#   def 자식메서드(self):
#       print("자식 메서드 호출")

# 부모클래스
class Parents:
    def __init__(self, name):
        self.p_name = name
        print('부모생성자')

    def parents_method(self):
        print('부모클래스 메소드')

class Child(Parents): # --> 상속받음
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print('자식생성자')

    def child_method(self):
        print('자식클래스 메소드')

# Child 클래스 객체 c
c = Child('홍길동', 20) # 객체 생성 시 클래스 변수? --> 출력 시 자식생성자
print(c.p_name, c.age) # AttributeError: 
# 그냥 상속받으면 메서드만 내려옴, 부모 init 호출 필요
