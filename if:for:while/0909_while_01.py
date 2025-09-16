# while 반복횟수가 없다
# while 조건 : 실행끝나고 회귀하여 다시 조건문 돌림, 무한루프
# Upper/Lower 함수 이용하면 대문자/소문자로 바꿔줌
import time

count = 0
while True :
    count += 1
    print(f'{count}초')
    time.sleep(1) # 1초간 지연
    
    # 5초 단위로 사용자한테 계속 할 건지 물어보기 "To be Continue(Y/N)"
    if count % 5 == 0:
        is_continue = input("To be Continue? (Y/N): ")

        if is_continue == 'Y':
        # if is continue = is_continue.upper()
            continue  # 계속 반복
        elif is_continue == 'N':
            print("종료합니다.")
            break  # 반복 종료
        else:
            print("잘못된 입력입니다. 다시 한 번 입력해주세요.")
            is_continue = input("To be Continue? (Y/N): ")
            if is_continue == 'Y':
        # if is continue = is_continue.upper()
                continue  # 계속 반복
            elif is_continue == 'N':
                print("종료합니다.")
            else :
                print("잘못된 입력입니다. 종료합니다.")
                break  # 반복 종료

