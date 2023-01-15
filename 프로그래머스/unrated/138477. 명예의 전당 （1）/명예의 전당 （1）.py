def solution(k, score):
    result = []
    low_rank = []
    for i in score :
        result.append(i)
        result.sort(reverse=True)
        if len(result) > k:
            result.pop()
        low_rank.append(result[-1])            
    return low_rank