#kor, eng, math 각 변수에 사용자로부터 값을 받아서
# avg 변수에 평균값을 저장하고
#  조건을 평균이 60점 이상이고 kor, eng, math 변수의 각 값이 40점 이상일때만
# 합격 출력 프로그램
kor = int(input('국어점수 입력')) # input()은 항상 문자열(str) 형태로 반환 --> 숫자 연산을 하려면 형변환 (int, float) 필요
eng = int(input('영어점수 입력'))
math = int(input('수학점수 입력'))
avg = (kor+eng+math)/3
if avg>=60 and kor >= 40 and eng >= 40 and math >= 40 :
    print('합격')
else :
    print('불합격')