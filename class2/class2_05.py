from abc import ABC, abstractmethod
class Parents(ABC):  # 부모가 ABC 상속받고 @abstractmethod 있을 때 기능 구현
    def make_money(self):
        raise NotImplementedError
    
    @abstractmethod # --> 강제화. 추상화는 상속하는 애들이 무조건 만들어야함, 안 그러면 객체 생성 불가
    def save_money(self):
        pass

class Child(Parents):
    def make_money(self): # 부모의 make_money 재정의(override)
        print('장사')
    def save_money(self):
        print('투자')

c = Child() # 부모의 추상메서드를 상속받았을 때 클래스에서 반드시 재정의 안 하면 객체 생성 불가
c.make_money() # 다형성  # 자식클래스에서 재정의 안 하면 예외 발생하도록 설계