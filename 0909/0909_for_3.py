# remove --> 결측치 지울 때 for문과 결합하여 사용?
# list_a=[1, 2, 1, 2]
# # list_a.remove(1)
# # print(list_a)
# for i in list_a :
#     list_a.remove(1)
# print(list_a)

#1 solution. ->에러 발생
# list_a=[1,2,1,2]
# index = -1 # 질문
# for i in list_a :
#     index +=1
    
#     print(f'index : {index} i : {i} list_a : {list_a}')

#     if i ==1 :
#         del list_a[index]
    
# print(list_a)

# 2 solution 정크데이터
# pass : 아무것도 안하는거, 그냥 두면 오류나니까 넣는거
# for i in range(len(list_a)):
# list_a = [1, 1, 1, 2]
# index = 0
# for i in list_a:
#     index -= 1
#     if list_a[i] == 1 :
#         del list_a[index] # --> 연구 필요, 실행결과 [1, 1]

# print(list_a)

# list_a = [1, 1, 1, 2]
# for i in range(3, -1, -1) :
#     if list_a[i] ==1 :
#         del list_a[i]

# print(list_a)

# solution3 remove() 이용 이 방법이 제대로 작동하는 방식
# list_a=[1,1,1,2]
# for i in range(len(list_a)):
#     if 1 in list_a :
#         list_a.remove(1)

# print(list_a)

list_a = [1,1,1,1,1,2,2,2,2,2,2]
for i in range(len(list_a)) :
    if 1 in list_a :
        list_a.remove(1)
    else :
        break # 더 이상 순환하지 않겠다는 뜻, 속도 더 빨리 처리    

print(list_a)

numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers :
    if number >= 100:
        print(f'100 이상의 수: {number}')

