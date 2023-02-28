def solution(n, s):
    result = [s // n for _ in range(n)]
    if s // n <= 0 :
        return [-1]
    if s % n == 0:
        return sorted(result)
    for i in range(s % n):
        result[i] +=1
    return sorted(result)