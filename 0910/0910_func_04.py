# 다양한 매개변수
    # 기본매개변수 default parameter
# def myAdd(num1, num2):
#     return num1 + num2

# result = myAdd(10, 20)
# print(f'result = {result}')

# def myAdd(num1, num2=30, num3): # num2 값 고정되어 있는 변수(기본 매개 변수) 중간에 있으면 안됨
# 값을 대입하는 과정에 오류 발생, 기본 매개 변수들은 뒤에 있어야 함. 그래야 대입 가능 
#     return num1 + num2

# result = myAdd(10)
# print(f'result = {result}')

def myAdd(num1 = 0, num2 = 0, num3 = 0):
    return num1+ num2+ num3

result1 = myAdd()
result2 = myAdd(10)
result3 = myAdd(10, 20)
result4 = myAdd(10, 20, 30) # 이렇게 되어있으면 디폴트에 대입 가능

print(result1, result2, result3, result4)