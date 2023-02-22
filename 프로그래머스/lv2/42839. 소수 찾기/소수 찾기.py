from itertools import permutations
import math
def check (num) :
    if num < 2:  
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
            

def solution(numbers):
    number = [num for num in numbers]
    check_num = []
    for i in range(1, len(numbers)+1):
        for j in permutations(number, i):
            check_num.append(int("".join(j)))
    result = [ch for ch in sorted(list(set(check_num))) if check(ch)]
    return len(result)