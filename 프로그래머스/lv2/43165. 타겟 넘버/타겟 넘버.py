def solution(numbers, target):
    answer = 0
    start_point = [[0,0]]
    while len(start_point) > 0:
        index, value = start_point.pop()
        
        if len(numbers) > index:
            start_point.append([index+1, value+numbers[index]])
            start_point.append([index+1, value-numbers[index]])
        
        if len(numbers) == index :
            if value == target:
                answer += 1
    return answer