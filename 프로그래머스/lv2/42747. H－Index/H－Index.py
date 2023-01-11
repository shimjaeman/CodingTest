def solution(citations):
    citations.sort(reverse=True)
    result = 0
    for i, j in enumerate(citations, 1):
        if i <= j :
            result = i
        else :
            return result
    
    return result