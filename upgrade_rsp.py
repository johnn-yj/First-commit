import random
print("컴퓨터와 하는 가위바위보 게임입니다.")
games = int(input("몇 판을 진행하시겠습니까? : "))
print("----------------------------------------")

def rsp_advanced(games):
    i,win,lose,draw=0,0,0,0
        
    while i<games:
        rsp_index = ["가위", "바위", "보"]
        computer = rsp_index[random.randint(0, 2)]
        
        inp_me = input("가위, 바위, 보 중 하나를 입력하세요: ")
        if (inp_me=="가위") or (inp_me=="바위") or (inp_me=="보"):
            i+=1
            if inp_me == computer:
                draw += 1
                number = 1
            elif (inp_me == "가위" and computer == "바위") or (inp_me == "바위" and computer == "보") or (inp_me == "보" and computer == "가위"):
                lose += 1
                number = 2
            else:
                win += 1
                number = 0
                         
            resultant = ("승리", "무승부", "패배")
            print("현재 게임 판 수: ", i, "판")
            print("나 : ", inp_me)
            print("컴퓨터: ", computer)
            print(i, " 번째 판 나의 ", resultant[number])
            print("----------------------------------------")
            
        else:
            print("다시 입력해주세요")
            

        
    print("나의 전적 : ", win, "승 ", draw, "무 ", lose, "패")
    print("컴퓨터의 전적 : ", lose, "승 ", draw, "무 ", win, "패")
    print("승률: ", (win/(win+draw+lose))* 100, "%")

rsp_advanced(games)