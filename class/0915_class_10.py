# 숫자 맞추기 게임
# 규칙
# 1. 컴퓨터가 1~100 사이의 숫자를 랜덤으로 선택
# 2. 사용자는 숫자를 입력하여 컴퓨터가 선택한 숫자를 맞춤
# 3. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 크면 "큽니다." 라고 출력
# 4. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자보다 작으면 "작습니다." 라고 출력
# 5. 사용자가 입력한 숫자가 컴퓨터가 선택한 숫자와 같으면 "정답입니다." 라고 출력 후 게임 종료
# 6. 사용자가 숫자를 맞출 때까지 계속 입력을 받음
# 7. 맞출 때까지 계속해야하니까 가위바위보랑 코드 느낌이 다름. 객체 생성 후 유지

import random

class Numberguessgame:
    def __init__(self):
        self.com_number = random.randint(1, 100)
        self.attempts = 0

    def guess(self, human_guess):
        self.attempts += 1
        if human_guess < self.com_number:
            return "작습니다"
        elif human_guess > self.com_number:
            return "큽니다"
        else:
            return True
    def human_guess(self):
        while True:
            try:
                guess = int(input("1부터 100사이의 숫자를 입력하세요."))
                if 1<= guess <= 100:
                    return guess
                else :
                    print("1부터 100사이의 숫자를 입력하세요")
            except ValueError:
                 print("숫자를 입력하세요")
    def game(self):
        while True:
            user_input = self.human_guess()
            result = self.guess(user_input)
            if result == True:
                print(f'정답입니다. 시도횟수 : {self.attempts}')
                break
            else:
                print(result)

Numberguessgame().game()