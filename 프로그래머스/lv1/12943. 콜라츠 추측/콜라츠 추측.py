def solution(num):
    cnt = 0
    count = 0
    while True :
        if num == 1 :
            break
        elif num % 2 == 0:
            num /= 2
            cnt += 1
        elif num % 2 == 1:
            num = (num * 3) + 1
            cnt += 1
        count += 1
        if count >= 500:
            cnt = -1
            break
    return cnt