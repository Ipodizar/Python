def change(obj):
    obj[0] = 100

data = [1, 2, 3]
change(data)
print(data)
print('-' * 30)
a = 10
b = a
b = 1000
print(f'a={a} b={b}')
print('-' * 30)

list_a = [1, 2, 3]
# list_b = list_a # 이름만 다른 애를 만들어서 쓰는거임. 주소값 자체가 복사. 쓸 때 조심해야 됨
# 우리가 생각하는 복사의 느낌으로 하려면
list_b = list_a.copy()
list_b[0] = 100
print(f'list_a = {list_a}.  list_b = {list_b}')