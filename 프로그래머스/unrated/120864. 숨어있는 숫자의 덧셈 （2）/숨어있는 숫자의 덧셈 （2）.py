import re

def solution(my_string):
    answer = list(map(int, re.findall(r'\d+', my_string)))
    return sum(answer)

