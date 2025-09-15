# 리스트
# 여러가지 자료를 저장할 수 있는 자료
# 대괄호 내부에 자료들 넣어 선언
age = 25
array = [273, 32, 103, "문자열", True, age]
print(array)
array_2 = [100, array]
print(array_2)
print(array_2[1][3])

temp = """[ 
[1, 2],     # temp[0] --row 행
[10, 20],   # temp[1] 
[30, 40]   # temp[2]
]""" # --> 행렬. 질문할 것

print(array[1][0])