def after_100():
    print("100일 계산기")
    print("========================================")
    d_day=input("언제사귀기 시작하셨습니까?(ex.20220812) : ")
    
    #날짜를 년,월,일로 구분
    year = int(d_day[:4])
    month = int(d_day[4:6])
    date = int(d_day[6:8])
    print(year, "년", month, "월", date, "일로부터 100일 뒤는")
    
    #월별 날짜 넣기
    month_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    month_day = month_list[month-1]
    
    #left_day로 날짜 계산
    left_day = month_day - (date-1)
    
    while True:
        #다음 월 넘어갈때 12월일때 년도가 넘어가고 1월으로 가도록
        if month==12:
            year=year+1
            month=month-11
        else:
            month=month+1

        #다음달로 넘어가서 날짜 계산, 100일 넘으면 출력 아니면 반복
        left_day = left_day + int(month_list[month-1])
        if left_day>=100:
            date_100=int(month_list[month-1])-(left_day-100)
            print(year, "년", month, "월", date_100, "일입니다.")
            break
        else:
            continue

    

after_100()