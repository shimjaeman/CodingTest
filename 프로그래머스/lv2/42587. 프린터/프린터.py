from collections import deque
def solution(priorities, location):
    atmos = deque([i,j] for i, j in enumerate(priorities))
    answer = 0
    while True:
        front = atmos.popleft()
        if any (front[1] < doc[1]  for doc in atmos):
            atmos.append(front)
        else :
            answer +=1
            if front[0] == location:
                break
    return answer