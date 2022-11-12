def solution(n):
    res = 0
    s = 1
    d = 1
    while s <= n:
        temp = s
        while temp <= n:
            if temp == n:
                res += 1
                break
            temp += d
        d += 1
        s += d
    return res