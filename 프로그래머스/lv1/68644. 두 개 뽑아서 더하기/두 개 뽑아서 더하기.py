def solution(numbers):
    answer=[]
    i = 0
    for a in range(i, len(numbers)):
        for b in range(i+1, len(numbers)):
            answer.append(numbers[a]+numbers[b])
        i += 1
    return sorted(set(answer))