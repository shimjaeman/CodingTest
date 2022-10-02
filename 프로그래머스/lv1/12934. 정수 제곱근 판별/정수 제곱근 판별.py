import math
def solution(number):
    if math.sqrt(number) == int(number**0.5):
        return (math.sqrt(number)+1)**2
    return -1