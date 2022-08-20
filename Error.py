
age_ = int(input("한국 나이를 입력하세요! : "))
birth = input("생일을 입력하세요(월/일): ").split("/")
today = input("오늘은 몇일입니까?(월/일): ").split("/")

for i in zip(birth , today):
    a = int (i[1]) - int(i[0])
    if a < 0:
        age_ = age_ - 2 
        break
    elif a > 0:
        age_ = age_ - 1
        break
    else:
        continue

print("당신의 미국나이는", age_ , "세 입니다,")