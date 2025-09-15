# 같은 이름일 떼 클래스 먼저, 그다음 정의한 함수

import random
class Person:
    def __init__(self, name, age):
        self.name = name  
        self._age = age    
    @property # 함수를 변수처럼 사용하고 싶을 때
    def age(self):
        return self._age
    @age.setter 
    def age(self, value):
        self._age = value

p1 = Person("홍길동", 20)
print(p1.age) # age함수로 사용하는 대신 괄호 안 붙임
p1.age = 30
