s = ["김갑,3242524215",
"이을,3242524223",
"박병,2242554131",
"최정,4245242315",
"정무,3242524315"]

a = [3,2,4,2,5,2,4,3,1,2]

def grader(s, a):
    성적 = []
    count = 1
    for 이름과답안지 in s:
        이름과답안지 = 이름과답안지.split(",")
        이름 = 이름과답안지[0]
        답안지 = list(이름과답안지[1])
        score = 0
        for i in range(len(답안지)):
            if int(a[i]) == int(답안지[i]) :
                score = score + 10
            else :
                score
        성적.append([score, 이름])
        성적.sort(reverse=True)
    for i in 성적:
        print("학생이름:", i[1], "점수:", i[0], "등수:", count)
        count += 1
grader(s, a)