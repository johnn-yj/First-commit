id = input('-를 포함한 주민등록번호를 입력하세요. : ')

def check_age(year, month, sex):
    if int(year) >=00 and int(year) <= 21:
        inp = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ")
        if inp == 'o':
            print(year,'년', month, "월", sex)
        elif inp == 'x':
            print("잘못된 번호입니다.") 
    else:
        print(year,'년', month, "월", sex)

def check_id(a):
    year = a[:2]
    month = a[2:4]
    sex = a[7]
    if len(a) == 14 and a[6] == '-':
        if sex == '1' or sex == '3':
            check_age(year, month, '남자')

        elif sex == '2' or sex == '4':
            check_age(year, month, '여자')
    else:
        print("주민등록번호를 다시 한 번 확인해주세요.")

check_id(id)