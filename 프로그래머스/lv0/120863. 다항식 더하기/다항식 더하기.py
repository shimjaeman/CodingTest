import re
def solution(polynomial):
    answer = polynomial.split(" + ")
    sum_x = 0
    sum_cnt = 0 
    for i in answer :
        if i[-1] == "x":
            if i[0] == "x":
                sum_x += 1
            else :
                sum_x += int(i[:-1])
        else :
            sum_cnt += int(i)
        
    if sum_cnt == 0:
        if sum_x == 1:
            return f"x"
        else :
            return f"{sum_x}x"
    elif sum_x == 0:
        return f"{sum_cnt}"
    else :
        if sum_x == 1:
            return f"x + {sum_cnt}"
        else :
            return f"{sum_x}x + {sum_cnt}"