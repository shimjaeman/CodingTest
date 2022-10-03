def solution(numbers):
    numbers.sort()
    return max(numbers[-1:])*max(numbers[-2:-1])