def solution(s):
    result = []
    for i in s:
        if not result:
            result.append(i)
        else :
            result.append(i)
            if result[-1] == result[-2]:
                result.pop()
                result.pop()
            else :
                pass
    return 1 if not result else 0