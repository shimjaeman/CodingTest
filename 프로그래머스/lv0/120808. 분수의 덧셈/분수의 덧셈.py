import math
def solution(denum1, num1, denum2, num2):
    a = num1 * num2
    b = denum2 * num1 + denum1 * num2
    gcd = math.gcd(b, a)
    return [b//gcd, a//gcd]