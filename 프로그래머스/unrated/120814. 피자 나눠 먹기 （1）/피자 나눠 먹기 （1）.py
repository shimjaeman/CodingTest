def solution(n):
    result = 0
    if n % 7 == 0:
        result = n//7
    elif n % 7 != 0:
        result = n//7 +1
    return result