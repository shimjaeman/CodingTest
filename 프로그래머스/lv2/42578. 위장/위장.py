def solution(clothes):
    clothes_dict = {}
    for name, tag in clothes:
        if tag in clothes_dict :
            clothes_dict[tag].append(name)
        else :
            clothes_dict[tag] = [ name ]
    
    answer = 1
    for k, v in clothes_dict.items():
        answer *= (len(v) + 1)
    answer -= 1
    return answer