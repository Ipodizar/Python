# 클래스 콜백함수
# __eq__ : ==
# __ne__ : !=
# __lt__ : < A < B
# __le__ : <= A <= B
# __gt__ : > A > B
# __ge__ : >= A >= B
class Student:
    def __init__ (self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f'이름 : {self.name}, 점수 : {self.score}'
    
    def __eq__ (self, other):
        return self.name == other.name

s1 = Student('홍길동', 90)
s2 = Student('홍길동', 90)

print(s1==s2)
print(s1)