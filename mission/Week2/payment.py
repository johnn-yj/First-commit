
def payment (income):
    reg_income = income*12
    t_rate = 6
    
    if reg_income <= 1200:
        t_rate = 6
    elif reg_income <= 4600:
        t_rate = 15
    elif reg_income <= 8800:
        t_rate = 24
    elif reg_income <= 15000:
        t_rate = 35
    elif reg_income <= 30000:
        t_rate = 38
    elif reg_income <= 50000:
        t_rate = 40
    else:
        t_rate = 42   

    real_income = int(reg_income*(100-t_rate)/100)
    print(income)
    print("당신의 세전 연봉은",reg_income,"만원입니다.")
    print("당신의 세후 연봉은 세율",t_rate,"%임에 따라",real_income,"만원입니다.")

m_income = int(input("본인의 월급을 숫자로 입력하세요(단위-만 원):"))
    #try :
    #    income = int(m_income)
    #except:
    #    print("한글이 아닌 숫자로 입력하세요")
payment(m_income)