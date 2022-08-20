#40시간을 초과한 시간의 시급을 1.5배하여 급여계산 프로그램 만들기
sh = input("Enter Hours: ")
sr = input("Enter Rates: ")
fh = float(sh)
fr = float(sr)

if fh > 40:
    print("Over time")
    regp = fr * fh
    otp = (fh-40.0)*(fr * 0.5) #왜 0.5? 이미 추가시간에 1.0배 기본급여는 받기때문에
    xp = regp + otp
else:
    print("regular")
    xp = fh * fr 
print("Pay:",xp)