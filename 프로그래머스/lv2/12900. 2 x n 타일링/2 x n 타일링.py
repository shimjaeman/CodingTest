def solution(n):
    class_1 = 1
    class_2 = 2
    result = 0
    if n == 1:
        return class_1
    elif n == 2:
        return class_2
    else :
        for i in range(n-2):
            tmp = class_1
            class_1 = class_2
            class_2 = tmp + class_1
        result = class_2 % 1000000007
    return result