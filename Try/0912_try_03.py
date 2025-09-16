# Exception : 모든 오류의 상위집합, 어머니같은 존재
# 디테일하게 하고 싶을 때는 Exception 자리에 오류 종류 적어줌

try :
    num1, num2 = map(int, input('공백을 기준으로 두 개의 숫자를 입력').split()) # split()으로 리스트로 변경 후 값 할당
    calc_lists = [num1 + num2, num1 - num2, num1 * num2, num1 / num2]

    print('1. 더하기', end = '\t') # \t : 이스케이프 시퀀스, tab과 같은 역할
    print('2. 빼기', end = '\t')
    print('3. 곱하기', end = '\t')
    print('4. 나누기', end = '\t')
    choice = int(input('원하는 결과를 입력하세요.'))
    print(f'결과는 = {calc_lists[choice-1]}')
except ValueError as e:
    print(f'오류발생 : {e}')
except IndexError as e:
    print(f'오류발생 : {e}')
except Exception as e:
    print(f'그 밖의 에러 : {e}')

print('프로그램 종료')
