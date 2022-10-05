def solution(numbers):
    num = sorted(numbers)
    num_len = len(num)
    return max(num[0]*num[1], num[num_len-1]*num[num_len-2])