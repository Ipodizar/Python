# 집합연산이 가능
import random
# list_a = random.sample(range(10), 6) # 0~9 중에 6개 추출
# list_b = random.sample(range(10), 7)
# find_list=[]
# for a in list_a :
#     for b in list_b :
#         if a==b :
#             find_list.append(a) # 교집합의 느낌

# print(f'list_a={list_a}')
# print(f'list_b={list_b}')
# print(f'find_list={find_list}')
list_a = random.sample(range(10), 6) # 0~9 중에 6개 추출
list_b = [1, 5, 4, 1, 2, 1, 5, 1, 7, 1]
find_list=[]
for a in list_a :
    for b in list_b :
        if a==b :
            find_list.append(a) # 교집합의 느낌

print(f'list_a={list_a}')
print(f'list_b={list_b}')
print(f'find_list={find_list}')
print(f'set(find_list)={set(find_list)}')
# 25라인에서 set을 사용하지 않고 원래 코드에서 중복 허용하지 않게 하기?