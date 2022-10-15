def minority (n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(n):
    result = 0
    for i in range(2, n+1):
        if minority(i) == True:
            result += 1
    return result
