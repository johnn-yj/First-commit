n = int(input("첫 번째 수 입력: "))
m = int(input("두 번째 수 입력: "))

def find_even_number(n, m):
    numbers = [i for i in range(n, m+1)]
    median = (n+m)/2

    for i in numbers:
        print("짝수")
        if i % 2 == 0:
            
            print(i)
            if i == median :
                print("중앙값: ", int(median))    
                
find_even_number(n,m)
