# 오류를 피해가는 행위 --> 예외 처리 try except
# try : 예외가 발생할 가능성이 있는 코드
# except : 예외가 발생했을 때 실행할 코드
# else : 예외가 발생하지 않았을 때 실행할 코드 / 근데 현업에서 잘 안씀...
# finally : 무조건 실행할 코드
# 예외 발생 가능성 있는 코드만 try 구문 내부에 넣고 나머지는 모두 else 구문으로 빼는 경우 많음
# 숫자를 입력받습니다.
# num_1 = int(input("숫자를 입력하세요."))
# num_2 = int(input("숫자를 입력하세요."))  

try :
    num1, num2 = map(int, input('공백을 기준으로 두 개의 숫자를 입력').split()) # split()으로 리스트로 변경 후 값 할당
    calc_lists = [num1 + num2, num1 - num2, num1 * num2, num1 / num2]

    print('1. 더하기', end = '\t') # \t : 이스케이프 시퀀스, tab과 같은 역할
    print('2. 빼기', end = '\t')
    print('3. 곱하기', end = '\t')
    print('4. 나누기', end = '\t')
    choice = int(input('원하는 결과를 입력하세요.'))
    print(f'결과는 = {calc_lists[choice-1]}')
except :
    print('오류발생')

print('프로그램 종료')

# 발생할 수 있는 오류의 종류 : 3가지

# 1. map에서 정수형이 아닌 숫자 입력
# 2. 나누기할 때 num2에 0을 넣는 경우
# 3. choice에서 이상한 인덱스 값 입력