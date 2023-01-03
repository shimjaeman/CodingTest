from collections import deque
import math
def lcm (a,b):
    return int(a*b / math.gcd(a,b))

def solution(arr):
    ans = 0
    deq = deque([])
    for i in arr:
        if len(deq) < 1:
            deq.append(i)
        else :
            deq.append(lcm(deq.pop(), i))
            
    return deq[-1]