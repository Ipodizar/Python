# 2명이서 진행하는 베스킨라빈스 31
# 1부터 시작해서 31을 말하는 사람이 지는 게임
# 전 사람이 말한 숫자에 연속되는 숫자를 말해야 함
# -->len(nums) >=1 and len(nums) <= 3
# 규칙을 어기는 사람은 반칙패
# 시작 순서는 랜덤으로
# 마지막 입력숫자 : current 변수 이용

# 1 시작 순서 정하기 --> random 이용. 0이 나오면 컴퓨터 먼저, 1이 나오면 사람 먼저
import random
def start_order() :
    players = ['Com', 'User']
    who_start = random.randint(0, 1)
    starter = players[who_start]
    print(f'{starter}가 먼저 시작합니다.')
    return starter

# 2 컴퓨터가 번호를 말하는 경우
# 숫자는 최대 3개이지만, 31을 넘어갈 수 없음
def com_game(current) :
    # 컴퓨터는 남은 숫자 수 만큼 제한하여 말해야 함, 예를 들어 29까지 선언됐을 때 최대 2개
    max_count = min(3, 31- current + 1)
    count = random.randint(1, max_count)
    nums = [current + i for i in range(count)]
    print(f'Com이 말한 숫자는 {nums}입니다.')
    return nums

# 3 유저가 번호를 말 하는 경우
def user_game(current) :
    print(f'User의 차례입니다. 현재 숫자는 {current}입니다.')
    user_input = input("1개부터 3개 사이의 연속된 숫자를 입력하세요")
    str_nums = user_input.strip().split()  # 
    nums = list(map(int, str_nums)) #
    # Com으로 부터 받은 숫자로부터 시작하지 않았을 때
    for i in range(len(nums)):     
        if nums[i] != current + i+ 1 :
            print(f'숫자를 {current + 1}부터 입력해야합니다.')
            return None
    # 1~3개 사이의 숫자를 입력하지 않았을 때
    if len(nums) < 1 or len (nums) > 3 :
        print("1개에서 3개사이의 숫자를 입력하세요")
        return None
    return nums

# 4 전체 게임
def baskin_robins_31() :
    print("베스킨라빈스 31! 베스킨라빈스 31")
    print("1~3개의 연속된 숫자를 말하세요. 31을 말하면 패배합니다.\n")

    players = ['Com', 'User']
    starter = start_order()
    turn = 0 if starter == 'Com' else 1

    current = 1

    while current < 31 :
        print(f'현재 숫자 : {current}')

        if players[turn%2] == 'Com' :
            nums = com_game(current)
        else:
            nums = user_game(current)
            if nums is None:
                print("반칙입니다. 컴퓨터 승리!")
                return

        current = nums[-1]  # 마지막 숫자 업데이트

        if current >= 31:
            loser = players[turn % 2]
            winner = players[(turn + 1) % 2]
            print(f"\n {loser}가 31을 말했습니다. {winner} 승리!")
            return

        turn += 1

baskin_robins_31()