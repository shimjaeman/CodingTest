
def solution(left, right):
    result = 0
    for i in range(left, right+1):
        count = 1
        for j in range(1, (i//2)+1):
            if i % j == 0 :
                count += 1
        if count % 2 == 0:
            result += i
        else :
            result -= i
    return result