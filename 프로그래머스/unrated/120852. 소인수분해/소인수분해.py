def solution(n):
    answer = []
    i = 2
    while True :
        if n == 1:
            break
        if n % i == 0:
            answer.append(i)
            n = n // i
        else :
            i +=1
    return list(dict.fromkeys(answer))