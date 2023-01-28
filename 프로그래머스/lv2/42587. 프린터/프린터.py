from collections import deque
def solution(priorities, location):
    my_doc = [0 for _ in range(len(priorities))]
    my_doc[location] = 1
    queue = deque(priorities)
    my_doc = deque(my_doc)
    answer = 0
    while True :
        # 인쇄를 다했거나 해당 문서를 인쇄한 경우
        if not my_doc or max(my_doc) != 1 :
            break
        # 첫번째 문서가 가장 중요도가 높은 경우:
        if max(queue) == queue[0]:
            queue.popleft()
            my_doc.popleft()
            answer +=1
        # 첫번째 문서가 가장 중요도가 높은 문서가 아닌경우 
        else :
            queue.append(queue[0])
            queue.popleft()
            my_doc.append(my_doc[0])
            my_doc.popleft()   
    return answer