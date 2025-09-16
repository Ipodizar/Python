list_a = [1, 2, 3]
print("리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()
list_a.insert(0, 10) # 잘 안씀
print(list_a)

list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")

# 제거 방법 [1] - del
del list_a[1]
print("del list_a[1]", list_a)

# 제거 방법 [2] - pop()
list_a.pop(0)
print("list_a.pop(0)", list_a)