# 중첩 for문
for i in range(3):
    for j in range(3):
        print(f'i : {i} j : {j}') # 안쪽 3번당 바깥쪽 1번
    print() # 순환종료 구분지어주려고