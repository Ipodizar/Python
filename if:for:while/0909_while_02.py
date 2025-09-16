# while 반복횟수가 없다
# while 조건 : 실행끝나고 회귀하여 다시 조건문 돌림, 무한루프
# Upper/Lower 함수 이용하면 대문자/소문자로 바꿔줌
import time

def display_second(count):
    count += 1 # count = count + 1
    print(f'{count}초')
    time.sleep(1) # 1초간 지연  
    return count 

def is_user_continue(count) :
    # 5초 단위로 사용자한테 계속 할 건지 물어보기 "To be Continue(Y/y)"
    if count % 5 == 0:
        user_input = input("To be Continue? (Y/y): ").upper()
        if not user_input == 'Y' :
            return False 
        return True
    else :
        return count
        

is_continue = True
count = 0
while is_continue :
    count = display_second(count) # 1초 간격으로 출력
    is_continue = is_user_continue(count) # 5초 단위로 진행여부 판단


        