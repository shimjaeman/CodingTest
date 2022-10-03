def solution(angle):
    if angle == 180 :
        result = 4
    elif angle > 90 :
        result = 3
    elif angle == 90 :
        result = 2 
    else : 
        result = 1
    return result