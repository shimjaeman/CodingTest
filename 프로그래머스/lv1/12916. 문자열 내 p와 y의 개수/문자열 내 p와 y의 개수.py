def solution(s):
    s = s.lower()
    answer1 = "p"
    answer2 = "y"
    a = s.count(answer1)
    b = s.count(answer2)
    
    return True if (a == b) else False # 모두 하나도 없는 경우도 0 == 0 이다.