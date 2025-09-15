# 파이썬 클래스에서 getter asetter 사용법
import random
class Person:
    def __init__(self, name, age):
        self._name = name # private 변수로 설
        정 클래스 밖에서는 못 사용함
        self._age = age # private 변수로 설정

a = Person("홍길동" , 25)