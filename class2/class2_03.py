# 직원 Employee - 아이디, 이름, 기본급
class Employee :
    def __init__(self, id, name, base_salary):
        self.id = id
        self.name = name
        self._base_salary = base_salary # private의 의미로 사용
    # 함수인데 변수처럼 사용 가능하게 해주는거 --> @property
    @property
    def base_salary(self):
        return self._base_salary
    
    @base_salary.setter
    def base_salary(self, money):
        if money > 0:
            self._base_salary = money
        else:
            raise ValueError('금액은 양수입니다.')
    def emp(self):
        print('직원클래스')
    def get_salary(self):
        return self.base_salary
    def __str__(self):
        return f'[직원] {self.name} (ID:{self.id}), 기본급: {self.base_salary:,}원'
    
# 정규직 FullTimeEmployee - 보너스

class FullTimeEmployee(Employee):
    def __init__(self, id, name, base_salary, bonus):
        super().__init__(id, name, base_salary)
        self._bonus = bonus
    # bonus도 마이너스 입력 불가
    @property
    def bonus(self):
        return self._bonus
    
    @bonus.setter
    def bonus(self, money):
        if money > 0:
            self._bonus = money
        else:
            raise ValueError('금액은 양수입니다.')
    def get_salary(self):
        return self.base_salary + self.bonus
    
    def __str__(self):
        return f'[정규직] {self.name} (ID:{self.id}), 기본급: {self.base_salary:,}원, 보너스: {self.bonus}원, 총 급여 : {self.get_salary()}'
    
    def fte(self):
        print('정규직 클래스')

# 계약직 PartTimeEmployee - 시간당 급여, 기본급 없음
class PartTimeEmployee(Employee):
    def __init__(self, id, name, base_salary, time_salary, hours):
        super().__init__(id, name, 0)
        self._time_salary = time_salary
        self._hours = hours
        # hourly_rate hours : getter setter
    @property
    def time_salary(self):
        return self._time_salary
    
    @time_salary.setter
    def time_salary(self, money):
        if money > 0:
            self._time_salary = money
        else:
            raise ValueError('금액은 양수입니다.')
        
    @property
    def hours(self):
        return self._hours
    
    @hours.setter
    def hours(self, hours):
        if hours > 0:
            self._hours = hours
        else:
            raise ValueError('시간은 양수입니다.')


    def get_salary(self):
        return self.time_salary * self.hours
    
    def __str__(self):
        return f'[계약직] {self.name} (ID:{self.id}), 시간급: {self.time_salary}원, 근무시간: {self.hours}h, 총 급여 : {self.get_salary()}'
    
    def pte(self):
        print("계약직 클래스")
    

# 인턴 Intern - 고정급만
class Intern(Employee):
    def __init__(self, id, name, base_salary, fixed_salary):
        super().__init__(id, name, 0)
        self.fixed_salary = fixed_salary

    def __str__(self):
        return f'[인턴] {self.name} (ID:{self.id}), 급여: {self.fixed_salary}원'
    
    def itn(self):
        print('인턴클래스')
    
# 정규직 직원, 계약직, 인턴을 모두 리스트에 섞어서 객체를 저장
# emp = [
#       FullTimeEmplyee(),
#       ...   
#        ]
# emp에 들어 있는 직원이 각각 어떤 클래스인지 순환문을 이용해서 각 클래스의 fte, pte, itn 메소드 호출 

emp = [
    FullTimeEmployee(1, '이순신', 3_000_000, 1_000_000),
    Intern(2, '나인턴', 0, 2_000_000),
    PartTimeEmployee(3, '계약직', 0, 15_000, 160),
    Intern(4, '취직좀', 0, 2_000_000),
    FullTimeEmployee(5, '나사장', 6_000_000, 10_000_000)
]

for e in emp:
    print(e)

    if isinstance(e, FullTimeEmployee):
        e.fte()
    elif isinstance(e, PartTimeEmployee):
        e.pte()
    elif isinstance(e, Intern):
        e. itn()

# emp 리스트의 각각의 객체에 해당하는 메소드를 호출 --> 다형성