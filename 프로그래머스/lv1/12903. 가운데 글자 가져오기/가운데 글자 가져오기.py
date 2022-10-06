def solution(s):
    len_s = len(s)-1
    return s[len_s//2] if len(s) % 2 == 1 else s[len_s//2:len_s//2+2]