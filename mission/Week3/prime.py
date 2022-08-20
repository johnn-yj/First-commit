n = int(input("첫 번째 수 입력: "))
m = int(input("두 번째 수 입력: "))

def count_prime_number(n, m):
    numbers = [i for i in range(n, m+1)]
    c_prime = 0
    for i in numbers:
        for j in range(2, i+1):
            if (i == j):
                c_prime = c_prime + 1
            elif (i % j == 0):
                break
    print(n,'과', m ,"사이의 소수 개수는:", c_prime, "개 입니다.")

count_prime_number(n,m)