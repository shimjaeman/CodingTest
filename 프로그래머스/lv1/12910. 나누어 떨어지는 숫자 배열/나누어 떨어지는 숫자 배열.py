def solution(arr, divisor):
    answer = []
    cnt = 0
    arr.sort()
    for p in arr:
        if p % divisor == 0:
            answer.append(p)
        else :
            cnt += 1
    if cnt == len(arr):
        answer.clear()
        answer.append(-1)
        return answer
    return answer