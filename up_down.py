import random

record = None

while True:
    print('Up&Down 게임 숫자를 맞추세요(1~100)')

    if record is None:
        print('현재 최고 기록 : 없음')
    else:
        print(f'현재 최고 기록 : {record}번')

    answer_number = random.randint(1, 100)
    # print(answer_number) 게임 확인용 정답출력
    count = 0

    while True:
        count += 1
        print(f'{count}번째 시도')

        try:
            my_guess = int(input('숫자를 입력하세요:'))
            if not (1 <= my_guess <= 100):
                print('1~100사이의 숫자를 입력하세요')
                continue
        except ValueError:
            print('숫자만 입력해 주세요')
            continue

        if my_guess == answer_number:
            print('정답입니다~!')
            print(f'{count}번째에 맞췄습니다.')
            if record is None or count < record:
                record = count
                print(f'최고 기록 달성 : {record}번')
            else:
                print(f'이번 기록 : {count}번')
            break
        elif my_guess > answer_number:
            print('Down~!')
        else:
            print('up~!')

    will_continue = input('다시 하겠습니까? (Y/N) ')

    if will_continue.upper() == 'Y':
        continue
    else:
        print('게임종료')
        break

print(f'최고 기록 : {record}번')
