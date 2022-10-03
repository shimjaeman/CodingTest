def solution(n):
    result = 0
    for i in range(1, n):
        if n % i == 1 :
            result = i
            break
    return result