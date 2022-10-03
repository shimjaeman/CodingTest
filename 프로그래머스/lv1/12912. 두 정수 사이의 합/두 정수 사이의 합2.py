def solution(a, b):
    result = 0
    if a <= b :
        for i in range(a, b+1) :
            result += i
    elif a > b :
        for i in range(b, a+1) :
            result += i
    return result
