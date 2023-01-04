def solution(n, lost, reserve):
    lost_a = sorted(set(lost) - set(reserve))
    reserve_a = sorted(set(reserve) - set(lost))
    for j in reserve_a :
        left = j-1
        right = j+1
        if left in lost_a:
            lost_a.remove(left)
        elif right in lost_a:
            lost_a.remove(right)
    return n - len(lost_a)