# 매개변수 o, 반환값 o
def multi_3(num1, num2, num3) :
    result = num1 * num2 * num3
    return result

print(multi_3(2, 4, 7))

# 매개변수 o, 반환값 x
def my_device(device) :
    print(f'내 기기는 {device} 입니다.')

my_device('맥북Air')

# 매개변수 x, 반환값 o
def five_only() :
    return 5

print(five_only())

# 매개변수 x, 반환값 x
def say_goodbye() :
    print('집갈거에요...')

say_goodbye()