# 리스트 컴프리핸션
total = []
for i in range(1, 11):
    total.append(i)

print(total)

# 좀 더 간단하게
print([i for i in range(1, 11)])
print([i+5 for i in range(1, 11)])

import random

total = []
for i in range(5):
    total.append(random.randint(1, 100))

print(total)

print([random.randint(1, 100) for i in range(5)])