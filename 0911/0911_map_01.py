# map 자료구조의 각 요소에 특정 함수를 적용
str_numbers = ['1', '10', '100']
print(str_numbers)
# map만 하면 어떻게 될 지 해보자
print(map(int, str_numbers))
print(list(map(int, str_numbers)))

scores = input('국어 영어 수학 점수를 공백을 기준으로 입력하세요')
# 숫자를 적어도 문자열로 들어간거임
scores = scores.split() # 공백을 기준으로 잘라줌, split(,)이면 , 기준으로 잘라줌
print(scores)
kor, eng, math = map(int, scores)
print(kor+eng+math)

list_2 = [10, 20, 30]
# 각 요소에 x2 다시 짜보자
# def test(data):
#     return data*2
# print(list(map(test, list_2)))
print(list(map(lambda data : data*2, list_2)))