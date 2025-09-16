# 순환문
import random
for i in range(3): # 3번 출력 index 값을 i에 대입, 굳이 i가 아니어도 되지만 다른 애들 규칙이 이럼
    print(f'출력 : {i}')

random_numbers = random.sample(range(100), 10)
# 짝수, 홀수 구분 출력
# 리스트를 순환한다
# 순환하면서 홀수인지, 짝수인지 구분하여 빈 리스트에 각각 추가
# 모든 순환이 끝나면 준비된 리스트 출력, len()이용해서 개수도 확인

even_numbers=[]
odd_numbers=[]
for i in random_numbers :
    if i%2 == 0 :
        even_numbers.append(i)
    else :
        odd_numbers.append(i)
even_numbers.sort()
odd_numbers.sort()

print(f'짝수 : {even_numbers}, 갯수 : {len(even_numbers)}')
print(f'홀수 : {odd_numbers}, 갯수 : {len(odd_numbers)}')