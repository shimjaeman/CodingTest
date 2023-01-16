def solution(s):
    answer =[]
    dct = dict()
    for i in range(len(s)):
        if s[i] not in dct:
            answer.append(-1)
        else :
            answer.append(i - dct[s[i]])
        dct[s[i]] = i
    return answer