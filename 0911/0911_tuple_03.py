# 튜플 VS 리스트는 서로 변경이 가능하다.
# 튜플 <--> 리스트 가능
list_a = [1, 2, 3]
tuple_a = (1, 2, 3)
print(f'type(list_a) = {type(list_a)}')
print(f'type(tuple_a) = {type(tuple_a)}')
print(tuple(list_a)) # 리스트 결과를 튜플로
list_a = tuple(list_a)
print(list_a)