import numpy as np
import pandas as pd

list_a = [1, 2, 3]
list_b = [4, 5, 6]
last_name = '홍'
first_name = '길동'
# 리스트 연산
print(f"list_a + list_b = {list_a + list_b}")
print(f'lilst_a * 2 = {list_a * 2}')

print(f'last_name + first_name = {last_name + first_name}')
print(f'last_name * 2 = {last_name * 2}')

list_c = np.array([1, 2, 3])
list_d = np.array([4, 5, 6])
list_e = np.add(list_c, list_d) 
print(list_e)
list_a.extend([4, 5, 6]) # list_a + list_b 와 동일, 다만 새로운 리스트명으로 해 줘야 할 듯?
print(list_a)

list_a = [1, 2, 3]
list_a += [4, 5, 6]
print(list_a)

list_a = [1, 2, 3]
list_a.extend(list_b)
print(list_a)