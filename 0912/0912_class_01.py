# 클래스 변수 VS 인스턴스 변수
# 함수 <-> 메소드 구분
# sep = \t 간격 띄우3

class StudentMng :
    name = '홍길동' # 클래스 변수
    def make_instance(self) : # self는 무조건 들어감
        self.age = 0
        self.addr = 0

# class StudentMng() :  # ()안에는 부모 class가 들어감. 상속. 하나만 들어감
#     name = '홍길동'

s1 = StudentMng()  #s1 : 객체 --> 클래스로 받은 값
s2 = StudentMng()
s3 = StudentMng()

s1.name = '이순신'
print(s1.name, s2.name, s3.name) # 인스턴스 변수 : 객체에 속한 독립적인 변수  이순신 홍길동 홍길동

s1.name = '강감찬'  # 인스턴스 변수 --> 주소값이 바껴버림. 디버깅 참고
# 가능하지만 애 안씀. 헷갈려버림. 클래스 변수는 클래스로만 접근할거임.
StudentMng.name = '이순신' # 클래스 변수
print(s1.name, s2.name, s3.name) # 강감찬 이순신 이순신  
# --> s2와 s3은 클래스 변수만 있고, s1은 인스턴스 변수와 클래스 변수 2개가 있는데, 인스턴스 변수가 덮어버림
# 자기만의 값을 가져버린 것
# 클래스 변수는 모든 객체가 참조하는 변수
# 그러나 객체가 변수를 재할당 받으면 해당 객체는 더 이상 참조하지 않는다.
