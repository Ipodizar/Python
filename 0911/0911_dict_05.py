# 선거 시스템
# 유권자들은 기호로 투표를 진행, 결과를 리스트에 저장
# Ex) 1, 2, 3
# 투표는 순환문을 이용해서 유권자가 10명이라면 10번 순환하면서 후보자 (1~5) 선택
#  [1, 1, 2, 3, 4, 1, 5, 1, 4, 3, 3]
# 리스트에 있는 각 번호의 횟수를 구해서 당선자를 출력
candidate = ['강민지', '홍길동', '이순신', '강감찬', '율곡']
vote = []
counts = 10 # 유권자
result = {} # 투표카운트
for _ in counts:
    vote.append(int(input('투표를 하세요 (1~5) : ')))
print(f'vote= {vote}')

# dict 기능을 이용

for i in vote :
    if i in result :
        result[i] += 1
    else : 
        result[i] = 1
print(f'result = {result}')

# 키의 값을 가져올 때 딕셔너리['키값'] 없으면 에러
# 딕셔너리변수 .get('키값') 없다면 None
# 가장 큰 값 찾는 함수, 딕셔네리에서는 뭐 없으면 key값 기준
max_key = max(result, key = result.get) # value값을 비교해서 가장 큰 key값 가져옴
# 당선자 key -1

print(f'당선자 : {candidate[max_key-1]} 득표수 : {result[max_key]}')



# 재미삼아 vote 랜덤
# import random
# result = [0]*5

# for i in vote:
#     result[i - 1] += 1

# for i in range(counts):
#     choice = random.randint(1, 5)
#     vote.append(choice)

# for i in range(5):
#     print(f"{candidate[i]} : result[i]표")

# max_votes = max(result)
# the_winner = result.index(max_votes)
# winner = candidate[the_winner]

# print(f"당선자는 {winner}입니다.")
