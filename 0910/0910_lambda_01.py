# 람다가 사용되지 않는 상황
# def add(a, b):
#     return a+b

# def minus(a, b):
#     return a-b
# def calc(func, a, b):
#     return func(a, b)

# print(calc(add, 1, 2))

def calc(func, a, b):
    return func(a, b)

print(calc(lambda a, b : a+b, 1, 2))
print(calc(lambda a, b : a*b, 3, 7)) # 한 번 쓰고 버리는 용도 ㅋ