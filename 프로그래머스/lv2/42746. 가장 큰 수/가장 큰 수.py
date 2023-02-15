def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda num : num * 3, reverse=True)
    return str(int("".join(numbers)))