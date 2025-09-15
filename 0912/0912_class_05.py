# 학생
# 이름, 학생 정보 출력
# 변수 : 이름, 나이
# 함수 : 학생 정보 출력

students = [] # 학생 이름 저장
class StudentMng() :
    def __init__(self):
        self.name = ''     # --> 변수
        self.age = 0

    def info_student(self) :
        print(f'이름 : {self.name} 나이 : {self.age}')  # --> 메소드

s1 = StudentMng()
s1.name = '홍길동'
s1.age = 25
students.append(s1)

s2 = StudentMng()
s2.name = '강감찬'
s2.age = 27
students.append(s2)

students[0].info_student()

# 학생정보 입력
# def create_student(name, age):
#     return students.append({'name' : name, 'age' : age}
#     {'name' : '홍길동', 'age' : 25}

# students.append(
#     {'name' : '이순신', 'age' : 35}
# )

# # 모든 학생 출력
# for s in students :
#     info_student(s)