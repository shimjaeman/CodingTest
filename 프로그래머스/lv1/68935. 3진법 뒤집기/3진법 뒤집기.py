def solution(n):
    result = []
    while True:
        if n < 1:
            break
        result += str(n % 3)
        n = n // 3
    third = "".join(result)
    return int(third, 3)