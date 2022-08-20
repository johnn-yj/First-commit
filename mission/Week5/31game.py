import random


def bs31():
    num = 0 # 현재 숫자를 저장하는 변수
    winner = "NONE" # 위너를 저장하는 변수
    print("베스킨라빈스 써리원 게임")
    print("----------------------")
    while(True): # 숫자가 31이 나와 종료될 때 까지(위너가 생기는 경우까지) 무한반복
        while(True): # 사용자가 올바른 입력을 할 때 까지 반복
            try:
                userIN = input("My Turn - 숫자를 입력하세요: ") # 입력받기
                userIN = userIN.split(" ") #입력받은 내용을 ' '로 분리하여 리스트화
                if(len(userIN) < 1 or len(userIN) > 3 or int(userIN[0]) != num+1): # 리스트의 길이가 1~3이 아니거나, 시작하는 숫자가 다음숫자가 아닌경우
                    raise Exception("WRONG INPUT") # 에러를 발생시켜 다시 입력하도록 유도
                for i in range(1, len(userIN)): # 나머지 리스트 요소들이 올바르게 입력되었는지 검사 
                    if(int(userIN[i-1])+1 != int(userIN[i])): # 요소가 1씩 차이나지 않는 경우
                        raise Exception("CHEAT INPUT") # 에러를 발생시켜 다시 입력하도록 유도
                num = int(userIN[len(userIN)-1]) # 검사가 완료되면 리스트의 마지막 요소로 num을 변경 
                if(num >= 31): # 사용자가 입력한 숫자에 31이 포함되었다면
                    winner = '컴퓨터' # 승자를 컴퓨터로 지정
                break # 무한반복 종료
            except:
                print("잘못 입력하셨습니다. 다시 입력해 주세요.")
        if (winner != "NONE"): # 승자가 새로 발생했다면
            print(f"{winner} 승리!") # 승자 출력
            break # 무한반복 종료
        print(f"현재 숫자: {num}") # 내가 입력한 숫자의 마지막 숫자를 표시
        computer = random.randint(1, 3) # 컴퓨터가 부를 숫자를 랜덤으로 정하기
        for i in range(1, computer+1):
            print(f"컴퓨터: {num+i}") # 컴퓨터의 숫자를 출력하면서 진행
            if (num+i == 31): # 컴퓨터가 선택한 숫자에 31이 포함된다면
                winner = '나' # 승자를 나로 설정
                break
        if (winner != "NONE"): # 승자가 변경되었다면
            print(f"{winner} 승리!") # 승자 출력
            break # 무한반복 종료
        num += computer # 컴퓨터의 숫자만큼 num 변경
        print(f"현재 숫자: {num}")


bs31()