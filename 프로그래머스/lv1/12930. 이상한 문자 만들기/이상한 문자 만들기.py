def solution(s):
    result = []
    answer = s.split(" ")
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            if j % 2 == 0 :
                result.append(answer[i][j].upper())
            else :
                result.append(answer[i][j].lower())
        result.append(" ")
    result.pop()
    return "".join(result)