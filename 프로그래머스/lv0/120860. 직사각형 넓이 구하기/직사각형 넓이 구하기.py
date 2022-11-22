def solution(dots):
    answer = sorted(dots, key = lambda x : [x[0], x[1]])
    a = answer[3][0] - answer[0][0]
    b = answer[3][1] - answer[0][1]
    return a * b