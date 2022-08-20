text1 = ""

while True:
    y = input('문장을 작성하세요: ')
    if y:
        text1 += y +'\n'
    else:
        break

file = open("text1.txt","w")
file.write(text1)
file.close()

keyword = str(input("어떤 글자의 반복 횟수를 알아 보시겠습니까? : "))
def count_txt(text, word):
    a = text.count(word)
    print("해당 글자는",a,"번 반복되었습니다.")

count_txt(text1, keyword)