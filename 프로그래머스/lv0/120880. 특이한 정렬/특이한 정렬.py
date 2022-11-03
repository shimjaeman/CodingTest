def solution(numlist, n):
    numlist = sorted(numlist, reverse=True)
    return sorted(numlist, key = lambda x : abs(x-n))