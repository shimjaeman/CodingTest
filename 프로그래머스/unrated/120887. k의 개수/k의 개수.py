def solution(i, j, k):
    return ([int(s) for p in range(i, j+1) for s in str(p)]).count(k)