print("미국 나이(만 나이) 계산기")
print("형식에 맞추어 순차적으로 입력하시면 미국 나이를 알려드립니다!")

age_ = int(input("한국 나이를 입력하세요! : "))
birth = input("생일을 입력하세요(ex:0918): ")
today = input("오늘은 몇일입니까?(ex:0717): ")

x = int(birth) - int(today) 
if x > 0:
    age_ = age_ - 2
    
else:
    age_ = age_ - 1
    
print("당신의 미국 나이(만 나이)는", age_ ,"세 입니다,")