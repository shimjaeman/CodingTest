def solution(hp):
    # 일개미 : 1 / 병정개미 : 3 / 장군개미 : 5
    attack = [5, 3, 1]
    count = 0
    for i in attack:
        count += hp // i
        hp %= i
    
    return count