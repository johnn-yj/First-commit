import random

print("컴퓨터와 함께하는 가위바위보 게임입니다!")
start_game = str(input("가위, 바위, 보 중 하나를 입력하세요: "))

def rsp (my_str):
    com_value = ["가위", "바위", "보"]
    computer = com_value[random.randint(0,2)]

    if my_str == "가위":
        print("당신의 선택:가위")
        if computer == "가위":
            print("컴퓨터의 선택:'가위'")
            print("무승부")
        elif computer == "바위":
            print("컴퓨터의 선택:'바위'")
            print("패배!")
        else:
            print("컴퓨터의 선택:'보'")
            print("승리!")
    elif my_str == "바위":
        print("당신의 선택:바위")
        if computer == "가위":
            print("컴퓨터의 선택:'가위'")
            print("승리!")
        elif computer == "바위":
            print("컴퓨터의 선택:'바위'")
            print("무승부")
        else:
            print("컴퓨터의 선택:'보'")
            print("패배!")
    elif my_str == "보":
        print("당신의 선택:보")
        if computer == "가위":
            print("컴퓨터의 선택:'가위'")
            print("패배!")
        elif computer == "바위":
            print("컴퓨터의 선택:'바위'")
            print("승리!")
        else:
            print("컴퓨터의 선택:'보'")
            print("무승부")
        
rsp(start_game)


