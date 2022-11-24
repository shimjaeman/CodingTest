def solution(nums):
    answer = len(nums) // 2
    n = len(list(set(nums)))
    if answer <= n:
        return answer
    return n