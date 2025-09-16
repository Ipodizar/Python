# 랜덤 라이브러리 가져오기
import random
# 랜덤 라이브러리 중에서 sample 함수 호출
# range(100) --> 0~99 범위에서 중복되지 않은 랜덤한 5개 추출
random_numbers = random.sample(range(100), 5) 
print(random_numbers) 
print(random_numbers[-1])

# 0~10 사이에 정수형 값 중에서 랜덤으로 한 개 생성
random_int=random.randint(0, 10)

random_numbers.append(random_int)

# 50이 있는지
print(50 in random_numbers)
print(random_numbers)

print('-'*50)

del random_numbers[0] # del은 뭐 지우는 지 모르고 그냥 지우는 느낌
print(random_numbers)
removed_number = random_numbers.pop(0)
random_numbers.pop(0) # pop()은 뭐 삭제하는 지 알려주고 삭제하는 느낌
print(random_numbers)
print(removed_number)