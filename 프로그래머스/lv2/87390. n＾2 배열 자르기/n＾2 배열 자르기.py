def solution(n, left, right):
    answer = [0 for i in range(right - left + 1)]
    i = 0
    while i < len(answer):
        x = (left // n) + 1
        y = (left % n) + 1
        answer[i] = max(x,y)
        i +=1
        left +=1
    return answer