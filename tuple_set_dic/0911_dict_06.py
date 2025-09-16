# 딕셔너리의 성질을 이용한 리스트의 요소를 카운트
# max함수를 이용해서 기준을 value로 바꿔서 가장 큰 value에 해당하는 key값 반환
# 매소드 .get() 사용

# 키를 이용해서 값을 가져오는 방법
dict_1 = {'사과' : 10, '포도' : 20}
# 포도의 값
print(dict_1['포도']) # 인덱스 방식. 없으면 keyerror
print(dict_1.get('포도')) # 매소드 방식.없으면 None
print(dict_1.get('파인애플', 0)) # 파인애플이 없으니 0  뒤에 0은 왜??
print(dict_1.get('포도', 0)) # 포도가 있으니 20

# 자료구조에서 가장 큰 값을 찾는 내장함수 max
print(max([1, 5, 2, 4, 8, 7, 1, 5, 4])) # 8이 출력

dict_1 = {'국어' : 80, '영어' : 100}
print(max(dict_1)) # key 값을 사전식으로 비교. 
# ㄱ, ㄴ, ㄷ, ..., ㅇ 이므로 가장 큰 Key 값인 영어 출력
print(max(dict_1, key = dict_1.get)) # value 값 비교해서 찾게 됨

# 정렬
list_1 = [5, 2, 1, 3]
print(sorted(list_1)) # 기본이 오름차순
print(sorted(list_1, reverse = True)) # 내림차순으로
print(sorted(list_1)[::-1]) # 처음부터 끝까지 뒤집어라

# dict
dict_1 = {'국어' : 80, '국사' : 100, '영어' : 98, '수학' : 80}
print(sorted(dict_1)) # Key를 기준으로 정렬
print(sorted(dict_1, key=dict_1.get)) # Value를 기준으로 key값을 정렬
#  key= 인자는 정렬 기준을 어떻게 할 것인지 지정하는 역할 수행
# dict_1.get은 함수입니다.
# 예: dict_1.get('국어') → 80, dict_1.get('국사') → 100
# 즉, 이 정렬은 각 key에 대해 해당하는 value를 기준으로 정렬하라는 뜻
