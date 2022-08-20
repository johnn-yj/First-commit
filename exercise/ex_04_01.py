#함수로 월급계산 프로그램 설정
def computepay(hours, rate):
    # print("Im computepay", hours, rate)

    if hours > 40:
        regp = rate * hours
        otp = (hours - 40.0)*(rate * 0.5) 
        pay = regp + otp
    else:
        pay = hours * rate 
    # print("Returning",pay)
    return(pay)


sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)  
fr = float(sr)

xp = computepay(fh, fr)

print("Pay:",xp)