def solution(n):
    cnt = 0
    for i in range(2, n+1):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                cnt +=1
                break
    return cnt