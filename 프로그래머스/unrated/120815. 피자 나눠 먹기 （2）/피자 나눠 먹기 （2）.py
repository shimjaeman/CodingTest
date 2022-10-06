def solution(n):
    cut, cnt = 6, 1 # 피자 조각수, 몇판
    for i in range(n) :
        if cut % n == 0:
            return cnt
        cut += 6
        cnt += 1
    return cnt