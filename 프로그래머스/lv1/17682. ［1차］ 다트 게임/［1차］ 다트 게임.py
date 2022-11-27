def solution(dartResult):
    answer = []
    for num, i in enumerate(dartResult, 1):
        if i == "S":
            answer[-1] = answer[-1] ** 1
        elif i == "D":
            answer[-1] = answer[-1] ** 2
        elif i == "T":
            answer[-1] = answer[-1] ** 3
        elif i == "*" : 
            answer[-1] = answer[-1] * 2
            if len(answer) >= 2:
                answer[-2] = answer[-2] * 2
        elif i == "#":
            answer[-1] = -answer[-1]
        else :
            if dartResult[num-1:num+1] == "10":
                answer.append(10)
            elif dartResult[num-2:num] != "10":
                answer.append(int(i))

    return sum(answer)