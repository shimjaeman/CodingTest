def solution(a, b):
    
    if b < a : b, a = a, b
    
    return sum(range(a, b+1))
