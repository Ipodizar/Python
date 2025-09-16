# 가위바위보 게임 (컴푸터 VS 휴먼)
# 가위 :1 바위 : 2 보 :3
# 규칙 : 컴퓨터가 임의로 숫자를 선택 : random
# 인간이 숫자를 입력              : input
# 승패를 기록                   
# 3번마다 계속할 지 물어본다        : 순환문 while / for문으로 안전하게?


import random
# 1 : 가위
# 2 : 바위
# 3 : 보

# 가위바위보 횟수 카운트
count = 0
human_win = 0
com_win = 0
while True :
# 랜덤하게 선택한 컴퓨터의 값
    com_choice = random.randint(1,3)
# 사용자의 값
    human_choice = int(input("입력(1: 가위, 2: 바위, 3: 보"))
# 승패
    if com_choice - human_choice == 0:
        print("비겼습니다")
        count += 1
        
    elif com_choice - human_choice == 1:
        print("컴퓨터 승!")
        count += 1
        com_win +=1
    else :
        print("인간 승!")
        count += 1
        human_win +=1

    if count %3 == 0 :
        user_input = input("To be continue? (Y/N)").upper()
        if user_input == "Y" :
            continue
        elif user_input == "N" :
            print("종료합니다.")
            break
        else :
            print("잘못된 입력입니다. 종료합니다.")
            break
           
print(f'컴퓨터 승리 횟수: {com_win}, 인간 승리 횟수: {human_win}')