def solution(n):
    answer = 0
    for i in range(1, n+1):
        s = 0
        while s < n:
            s += i
            i += 1
        if s == n:
            answer +=1
    return answer