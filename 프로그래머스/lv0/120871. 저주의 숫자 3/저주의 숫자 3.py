def solution(n):
    answer = []
    a, b = 0, 0
    while True :
        a += 1 # result 숫자 +1
        if b > n :
            break
        if a % 3 != 0 and "3" not in str(a):
            answer.append(a)
            b += 1
    return answer[n-1]