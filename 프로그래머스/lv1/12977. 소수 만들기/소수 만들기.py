import math
from itertools import combinations
def solution(nums):
    result = 0
    for i in combinations(nums, 3):
        sum_num = sum(i) 
        count = 0
        for j in range(2, int(sum_num//2)+1):
            if sum_num % j == 0:
                break
        else:
            result+=1
    return result