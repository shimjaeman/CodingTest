def solution(n):
    d = [0 for _ in range(2001)]
    d[1] = 1
    d[2] = 2
    if n < 3:
        return d[n]
    
    for i in range(3, n+1):
        d[i] = (d[i-1] + d[i-2]) % 1234567
    return d[n]