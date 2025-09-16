# 사용자로부터 점수를 입력받아서 A B C D F 학점을 출력
score = int(input('총점을 입력하세요 : '))
print(f'score={score}')
if score >= 90 :
    # 점수 90점 이상
    print('A')
elif score >= 80 :
    # 점수 80점 이상 90점 미만
    print('B')
elif score >= 70 :
    # 점수 70점 이상 80점 미만
    print('C')
elif score >= 60 :
    # 점수 60점 이상 70점 미만
    print('D')
else : 
    # 점수 60점 미만
    print('F')