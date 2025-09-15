# isinstance() 함수
# 객체가 특정 클래스의 인스턴스(객체)인지 확인
# 사용하는 이유
# 1. 타입 체크 : 함수나 메소드가 특정 타입의 객체만 처리하도록 제한하고 싶을 때
# 2. 다형성 지원 : 여러 클래스가 동일한 메소드를 가지고 있을 때, 객체의 실제 타입에 따라 다른 동작을 수행하도록 할 때
class Student:
    def study(self):
        return "학생이 공부합니다."
class Teacher:
    def teach(self):
        return "선생님이 가르칩니다."
    
# 리스트에 어떤 객체가 있는지 모를때 특정 인스턴스만 기대할 수 없다.
people = [Student(), Teacher(), Student()]
# people[0].teach() # AttributeError: 'Student' object has no attribute(속성)인'teach' 가 없다.
if isinstance(people[0], Student):
    print(people[0].study())
else:
    print(people[0].teach())