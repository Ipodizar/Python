# 딕셔너리 생성
# 딕셔너리에서 값을 출력
# 딕셔너리에서 값을 추가
# 딕셔너리에서 값을 삭제
# 딕셔너리 특정 키의 데이터를 수정
# enumerate(), zip(), items(), keys(), values()
# map(), 정렬 --> 람다함수를 적용
# 함수의 파라메터 --> 키워드 파라메터, 가변 키워드 파라메터

stu_info = dict(
    name = ["차무식", "엄홍상", "트럼프"],
    height = ["178cm", "173cm", "187cm"],
    weight = ["85kg", "65kg", "90kg"]
)
print(stu_info)
stu_info["name"].append("레옹")
stu_info["height"].append("165cm")
stu_info["weight"].append("50kg")
print(stu_info)
del stu_info["name"]
print(stu_info)
stu_info["addr"] = ["서울특별시", "경기도", "미국", "프랑스"]
print(f'stu_info = {stu_info}')

# 예제2
my_bag = {'필통' : '파란색', '공책' : '수학공책', '지갑' : '분홍색'}
print(my_bag)
# 가방에서 필통을 꺼내서 출력 print(my_bag['필통'])
print(my_bag.keys())
# 가방에서 공책을 꺼내서 출력 print(my_bag['공책'])
print(my_bag.values())
# 지갑이 오래되어서 "가죽지갑" 변경 
my_bag['지갑'] = '가죽지갑'
print(my_bag)
# 물통을 추가 하얀색으로
my_bag['물통'] = '하얀색'
print(my_bag)
# 공책을 다 써서 버려주세요
del my_bag['공책']
print(my_bag)
# ------순환문과 연결---------
for i in my_bag :  
    # print(i)  #for문 사용 시 기본적으로 Key값 순환
    print(f'key = {i}, value = {my_bag[i]}')

# for key, value in my_bag.items():
    # print(f"{key} : {value}")   --> 요렇게도 가능