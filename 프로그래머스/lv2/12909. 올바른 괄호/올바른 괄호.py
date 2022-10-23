from collections import deque
def solution(s):
    answer = True
    count = 0
    que = deque(s)
    while (que):
        check = que.popleft()
        if check == "(":
            count +=1
        else :
            count -=1
            
        if count < 0:
            answer = False
            break
            
    if count > 0:
        answer = False
        
    return answer
    