# 다양한 매개변수
    # 기본매개변수 default parameter
# def myAdd(num1, num2):
#     return num1 + num2

# result = myAdd(10, 20)
# print(f'result = {result}')

def myAdd(num1, num2=30):
    return num1 + num2

result = myAdd(10)
print(f'result = {result}')

