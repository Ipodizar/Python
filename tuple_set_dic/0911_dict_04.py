
employee_info = {
    '홍길동' : {
        '직책' : '매니저',
        '연봉' : 200000000,
        '경력' : {
            '삼성전자' : '5년',
            'LG전자' : '3년',
            'SK' : '10년'
        },
        '취미' : ['골프', '헬스', '수영']
    }
}

print(employee_info['홍길동']['경력']['SK'])

# 학생이 시험 보는 과목이 국어, 영어, 수학 3과목. 점수관리
#''' '''  --> 주석처리, 실행 안됨


student1 = [100, 80, 95]
student2 = [90, 85, 90]
student3 = {'국어' : 100, '영어' : 100, '수학' : 90}
student4 = {'영어' : 100, '수학' : 85, '국어' : 100}
student5 = {'수학' : 75, '국어' : 100, '영어' : 100}

element_class = [student3, student4, student5]

# 3, 4, 5의 수학 점수를 다 더하고 싶다
# 컴퓨터는 한 번에 다 못 하니까 한 번씩 순환문으로

total_math = 0
for student in element_class :
    total_math += student['수학']

print(f'수학 점수의 총합은 {total_math}점 입니다.')