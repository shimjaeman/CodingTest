dict_a = {"left":[1,4,7], "right":[3,6,9], "center":[2,5,8,0]}
dict_geo = {"1": (0,0), "2": (0,1), "3":(0,2),
            "4": (1,0), "5": (1,1), "6":(1,2),
            "7": (2,0), "8": (2,1), "9":(2,2),
            "*": (3,0), "0": (3,1), "#":(3,2)}

# 거리 함수계산
def space(number, pos): 
    number = str(number)
    pos = str(pos)  
    x_number, y_number = dict_geo[number]
    x_pos, y_pos = dict_geo[pos]
    return abs(x_number - x_pos) + abs(y_number - y_pos)

def solution(numbers, hand):
    R = "#"
    L = "*"
    result =""
    for num in numbers:
        if num in dict_a["left"]:
            result += "L"
            L = str(num)
        elif num in dict_a["right"]:
            result += "R"
            R = str(num)
        elif num in dict_a["center"] :
            L_C_space = space(num, L)
            R_C_space = space(num, R)
            if L_C_space== R_C_space :
                if hand == "right":
                    result += "R"
                    R = str(num)
                else:
                    result += "L"
                    L = str(num)
            elif L_C_space < R_C_space :
                result += "L"
                L = str(num)
            elif L_C_space > R_C_space:
                result += "R"
                R = str(num)
            else : 
                pass
    return result