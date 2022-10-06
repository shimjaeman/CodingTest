def solution(before, after):
    bef = sorted([i for i in before])
    aft = sorted([i for i in after])
    for i in range(len(bef)):
        if bef[i] != aft[i]:
            return 0
            
    return 1