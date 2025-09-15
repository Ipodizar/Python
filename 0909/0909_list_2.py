list_a = [91, 2, "문자열", True, False]
print(list_a[2][2])
print(list_a[ : ]) # start_index : end_index-1. # 원본을 복사
print(list_a[ : 3])
print(list_a[3 :])
print(list_a[-1])
# start index : end index -1 : 1
print(list_a[::2])  # 간격 2씩
print(list_a[::-1]) # 역순 출력

# 리스트를 선언합니다.
list_a=[1,2,3]
list_b=[4,5,6]
print(list_a + list_b)
print(list_a * 3)
print(len(list_a))
for i in list_a :
    if i == 1 :
        list_a.remove(i)
print(list_a)
print("len(list_a)", len(list_a))
print(f'len(list_a) {len(list_a)}')