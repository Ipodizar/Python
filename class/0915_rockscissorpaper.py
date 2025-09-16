# 가위바위보 게임을 클래스로 구현
# 사용자로부터 입력을 받아 컴퓨터와 대결
# 사용자는 가위, 바위, 보 중에 하나 입력, 컴퓨터는 무작위로 선택
# 게임의 승패 판단하고 결과 출력
# 가위는 1, 바위는 2, 보는 3으로 표현
# 게임 종료 시 게임을 계속할 지 물어본다.

import random

class Rockscissorpaper:
    def __init__(self):
        self.user_input = {1 : '가위', 2 : '바위', 3 : '보'}
        self.user_point = 0
        self.computer_point = 0

    def get_user_choice(self):
        while True :
            try :
                user_input = int(input('가위' : 1, '바위' : 2, '보' : 3 중에 입력하세요))
                if user_input in self.user_input :
                    return user_input
                else :
                    print(f'{user_input}은 잘못된 입력입니다. 1, 2, 3 중에 입력해주세요')
            except ValueError:
                print("숫자를 입력하세요")
                