def solution(array, commands):
    result = []
    answer = []
    for com in commands:
        sort_com = sorted(array[com[0]-1:com[1]])
        result.append(sort_com[com[2]-1])
        
    return result