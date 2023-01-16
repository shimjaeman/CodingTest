import math
from itertools import combinations
def solution(nums):
    result = 0
    for i in combinations(nums, 3):
        sum_num = sum(i) 
        count = 0
        for j in range(2, sum_num+1):
            if sum_num % j == 0:
                count +=1 
        if count == 1:
            result+=1
    return result