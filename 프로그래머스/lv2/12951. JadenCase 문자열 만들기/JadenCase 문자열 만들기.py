def solution(s):
    result = []
    result.append(s[0].upper())
    for i in range(1, len(s)):
        # 숫자가 있고 and 숫자 앞에 
        if s[i-1] == " " and s[i] != " ":
            result.append(s[i].upper())
        else:
            result.append(s[i].lower())
    return "".join(result)