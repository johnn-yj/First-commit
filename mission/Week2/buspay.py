c_c = str(input("현금/카드 중 하나를 입력해주세요: "))
age_n = int(input("나이를 입력해주세요): "))

def buspay (payWay, age):
    print("나이: ",age, "세")
    if(payWay == "카드"):
        print("지불유형: 카드")
        if(age < 8):
            pay = 0
        elif(age >= 8 and age < 14):
            pay = 450
        elif(age >= 14 and age < 20):
            pay = 720
        elif(age >= 20 and age <=74):
            pay = 1200
        else:
            pay = 0
        print("버스요금은",pay,"원입니다.")

    else:
        print("지불유형: 현금")
        if(age < 8):
            pay = 0
        elif(age >= 8 and age < 14):
            pay = 450
        elif(age >= 14 and age < 20):
            pay = 1000
        elif(age >= 20 and age <= 74):
            pay = 1300
        else:
            pay = 0
        print("버스요금은",pay,"원입니다.")
buspay(c_c, age_n)