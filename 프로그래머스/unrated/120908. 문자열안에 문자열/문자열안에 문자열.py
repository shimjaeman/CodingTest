def solution(str1, str2):
    for i in range(len(str1)+1):
        if str1[i:len(str2)+i] == str2:
            result = 1
            break
        else :
            result = 2
    return result
    