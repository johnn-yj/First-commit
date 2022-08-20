number = input('몇단을 확인할까요?: ')

def t_table (num):
    try:
        print(number,'단')        
        for num in [1,3,5,7,9]:
            table = int(number) * num
            if table <= 50:
                print(number,'*',num,'=',table )
            else:
                break
    except:
        print('Please Enter a number')
        
t_table(number)