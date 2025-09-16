# 사용자 입력 처리 함수
# 이름 get_data()
# 파라메터
    # start : 시작값
    # end : 종료값 
    # input_str : 가이드문구
# 사용자 입력은 input()
# return 정수로 변환된 입력값

# while True :
    # try:
    #     h_nmum = int(input('정수를 입력하세요 (1 ~ 100)'))
    #     if not 0 <= h_nmum <= 100:
    #         raise ValueError('1 ~ 100 범위 초과')
    # except Exception as e:
    #     print(f'오류 : {e}')
    # else:
    #     break

def human_number() :
    
    while True:
        try:
            i = int(input('정수를 입력하세요 (1 ~ 100)'))
            if not 0 <= i <= 100:
                raise ValueError('1 ~ 100 범위 초과')
        except Exception as e:
            print(f'오류 : {e}')
        else:
            print(f'{i}는 올바른 입력값입니다. 종료합니다.')
            return # 함수 자체를 종료해버림, break와 같은 역할

human_number()
