import random

choices = ["가위", "바위", "보"]

wins = 0
loses = 0
draw = 0

while True:
    user_choice = input("가위, 바위, 보 중 하나를 선택하세요 : ")
    print("당신은" + user_choice + "를 냈습니다.")

    if user_choice not in choices:
        print("잘못된 입력입니다.")
        continue

    pc_choice = random.choice(choices)
    print("pc는" + pc_choice + "를 냈습니다.")

    if user_choice == pc_choice:
        print("비겼습니다.")
        draw += 1
    elif (user_choice == "가위" and pc_choice == "보") or (user_choice == "바위" and pc_choice == "가위") or (user_choice == "보" and pc_choice == "바위"):
        print("승리!")
        wins += 1
    else:
        print("패배ㅜ")
        loses += 1

# 한영키 전환 귀찮으니 1,2 로 설정
    will_continue = input('한판 더? (다시하기 : 1 / 그만하기 : 2) ')
    if will_continue.upper() == '1':
        continue
    elif will_continue == '2':
        print(f"전적 : {wins}승, {draw}무, {loses}패")
        print('게임종료')
        break
    # 1,2 가 아닐경우 나오는 문구
    else:
        print("1또는 2만 입력해 주세요.")
        break
