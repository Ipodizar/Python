# 함수
# 함수명 add
# 파라메터는 2개 op1, op2
# 결과를 반환한다

def add(op1, op2):
    result = op1 + op2
    return result

# 사용
print(add(10, 20))
two_nummber_hab = add(10, 30)
numbers = [add(10, 2), add(100, 20)]

# 매개변수 받아서 출력하는 함수
# 함수명 : show_number
# 매개변수명 : data
def show_number(data) :
    print(f'numbers = {data}')

show_number(add(10, 2))

def len_str(data):
    count = 0
    for _ in data:
        count +=1
    return count

len_str("안녕하세여")
print(count)

