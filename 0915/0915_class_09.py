# 가위바위보 게임을 클래스로 구현
# 사용자로부터 입력을 받아 컴퓨터와 대결
# 사용자는 가위, 바위, 보 중에 하나 입력, 컴퓨터는 무작위로 선택
# 게임의 승패 판단하고 결과 출력
# 가위는 1, 바위는 2, 보는 3으로 표현
# 게임 종료 시 게임을 계속할 지 물어본다.
# 객체 하나가 게임 하나
import random

class RockPaperScissors:
    def __init__(self):
        self.choices = {1: '가위', 2: '바위', 3: '보'}
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        while True:
            try:
                user_input = int(input("가위(1), 바위(2), 보(3) 중 하나를 선택하세요: "))
                if user_input in self.choices:
                    return user_input
                else:
                    print("잘못된 입력입니다. 1, 2, 3 중 하나를 선택하세요.")
            except ValueError:
                print("숫자를 입력하세요.")

    def get_computer_choice(self):
        return random.randint(1, 3)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "무승부"
        elif (user_choice - computer_choice == -1):
            return "사용자 승리"
        else:
            return "컴퓨터 승리"
        
    def play(self):
        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            print(f"사용자 선택: {self.choices[user_choice]}, 컴퓨터 선택: {self.choices[computer_choice]}")

            result = self.determine_winner(user_choice, computer_choice)
            print(result)

            if result == "사용자 승리":
                self.user_score += 1
            elif result == "컴퓨터 승리":
                self.computer_score += 1

            print(f"현재 점수 - 사용자: {self.user_score}, 컴퓨터: {self.computer_score}")

            
            play_again = input("게임을 계속하시겠습니까? (Y/N): ").strip().upper() # 입력한 거 공백 제거
            if play_again == 'Y':
                print("게임을 종료합니다.")
                break

RockPaperScissors().play() # 객체 생성할 필요가 없음

