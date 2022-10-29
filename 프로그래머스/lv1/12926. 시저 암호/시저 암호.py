def solution(s, n):
    result=""
    for i in s:
        if 65 <= ord(i) <= 90:
            if 65 <= ord(i) + int(n) <= 90:   # 대문자
                result += chr(ord(i) + int(n))
            elif ord(i) + int(n) > 90 : 
                result += chr(ord(i) + int(n) - 26)
            else :
                result += i
        if 97 <= ord(i) <= 122:
            if 97 <= ord(i) + int(n) <= 122:   # 소문자
                result += chr(ord(i) + int(n))
            elif ord(i) + int(n) > 122 : 
                result += chr(ord(i) + int(n) - 26)
            else :
                result += i
        if i == " ":
            result += i
    return result

# a-z => 97-122
# A-Z => 65-90