from collections import deque
def solution(prices):
    price_deq = deque(prices)
    answer = [0 for i in range(len(prices))]
    cnt = 0
    while price_deq:
        check_second = price_deq.popleft()
        for i in price_deq:
            if check_second <= i:
                answer[cnt] += 1
            else :
                answer[cnt] += 1
                break
        cnt +=1 
    return answer
