from collections import deque
def solution(s):
    answer = deque([])
    s = s.split(" ")
    for i in s:
        if i == "Z":
            answer.pop()
        else :
            answer.append(int(i))
    return sum(answer)