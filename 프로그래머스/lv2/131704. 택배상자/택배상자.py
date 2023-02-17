from collections import deque
def solution(order):
    new_belt = []
    que = deque(order)
    answer = 0
    for i in range(1, len(order)+1):
        new_belt.append(i)
        while new_belt and que[0] == new_belt[-1]:
            answer +=1
            new_belt.pop()
            que.popleft()
    return answer