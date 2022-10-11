def solution(s):
    if len(s) == 4 or len(s) == 6:
        if str.isdigit(s):
            return True
        else :
            return False
    else:
        return False