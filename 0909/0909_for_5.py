# 중첩 for문 2
import numpy as np

list_1 = [10, 20, 30]
list_2 = [11, 22]

list_2nd = [list_1, list_2]
for row in list_2nd :
    print(row)

for i in range(len(list_2nd)) :
    for j in range(len(list_2nd[i])):
        print(f'list_2nd[{i}][{j}] {list_2nd[i][j]}')

# np.list_1 = [10, 20, 30]
# np.list_2 = [11, 22, 33]
# print(np.list_1 \n np.list_2)

# For문 : 반복횟수 지정. 무한정 아님