import games_function as gu
import random as rd
start, end = 1, 100

computer = rd.randint(start,end)

count = 0
game_history = []
while True:
    count += 1
    human = gu.get_data(start,end)    
    # 승자 선택 로직
    if gu.checK_winner(human, computer, game_history, count):
        break


# 코드 분석 순서
# 1. 게임 기본 코드 분석
# 2. count와 같은 부수적인 코드 분석
# 3. 모듈화