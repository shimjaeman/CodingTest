def solution(d, budget):
    cnt = 0
    for ans in sorted(d):
        if budget - ans >= 0:
            budget -= ans
            cnt +=1
    return cnt # 최대 몇 개의 부서에 물품을 지원