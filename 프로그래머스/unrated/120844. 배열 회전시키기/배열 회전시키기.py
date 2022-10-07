def solution(numbers, direction):
    answer = []
    num_len = len(numbers)
    for id in range(num_len):
        if direction == "right":
            if id == (num_len-1) :
                answer.insert(0, numbers[id])
            else :
                answer.append(numbers[id])
        else :
            if id == 0 :
                answer.insert(-1, numbers[id])
            else :
                answer.insert(-1, numbers[id])
    return answer