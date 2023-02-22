def solution(n):
    result = ""
    num_124 = {0 : "1", 1 : "2", 2 : "4"}
    while n > 0:
        n -= 1
        result += num_124[n % 3]
        n //= 3
    return result[::-1]