inp_name = str(input("이름을 입력해주세요: "))
inp_score = int(input("성적을 입력해주세요(0~100): "))

def grade(name, score):
    
    if (score >100):
        print("Error")
    elif(score >= 95 ):
        s_grade = "A+"
    elif(score >= 90):
        s_grade = "A"
    elif(score >= 85):
        s_grade = "B+"
    elif(score >= 80):
        s_grade = "B"
    elif(score >= 75):
        s_grade = "C+"
    elif(score >= 70):
        s_grade = "C"
    elif(score >= 65):
        s_grade = "D+"
    elif(score >= 60):
        s_grade = "D"
    else:
        s_grade = "F"
    print("학생 이름:",name)
    print("점수:",score)
    print("학점:",s_grade)

grade(inp_name, inp_score)