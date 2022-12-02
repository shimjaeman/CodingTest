def result(quiz):
    quiz = quiz.split(" ")
    if quiz[1] == "-":
        if (int(quiz[0]) - int(quiz[2])) == int(quiz[-1]):
            return "O"
        else :
            return "X"
    if quiz[1] == "+":
        if (int(quiz[0]) + int(quiz[2])) == int(quiz[-1]):
            return "O"
        else :
            return "X"

def solution(quiz):
    answer = []
    for i in quiz:
        answer.append(result(i))
    return answer