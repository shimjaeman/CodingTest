dict_a = {"left":[1,4,7], "right":[3,6,9], "center":[2,5,8,0]}
dict_geo = {"1": (0,0), "2": (0,1), "3":(0,2),
            "4": (1,0), "5": (1,1), "6":(1,2),
            "7": (2,0), "8": (2,1), "9":(2,2),
            "*": (3,0), "0": (3,1), "#":(3,2)}

def space (number, pos):
    number = str(number)
    pos = str(pos)
    number_x, number_y = dict_geo[number]
    pos_x, pos_y = dict_geo[pos]
    return abs(number_x - pos_x) + abs(number_y - pos_y) 

def solution (numbers, hand):
    left_pos = "*"
    right_pos = "#"
    answer = ""
    for num in numbers :
        # [1,4,7]
        if num in dict_a["left"]:
            answer += "L"
            left_pos = str(num)
        # [3, 6, 9]
        elif num in dict_a["right"]:
            answer += "R"
            right_pos = str(num)
        # [2, 5, 8, 0]
        elif num in dict_a["center"]:
            left_space = space(num, left_pos)
            right_space = space(num, right_pos)
            if left_space == right_space:
                if hand == "right":
                    answer += "R"
                    right_pos = str(num)
                elif hand == "left" :
                    answer += "L"
                    left_pos = str(num)
            elif left_space > right_space:
                answer += "R"
                right_pos = str(num) 
            elif left_space < right_space:
                answer += "L"
                left_pos = str(num)
            else :
                pass
    return answer