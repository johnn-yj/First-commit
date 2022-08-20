#루프 종료 메커니즘
#입력값 예외 처리
#continue , break

num = 0
total = 0.0
while True :
    sval = input('Enter a Number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid value')
        continue
    #print(fval)
    num = num + 1
    total = total + fval 

#print('ALL DONE')
print(total, num, total/num)
