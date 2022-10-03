def solution(my_string):
    result = [i for i in my_string if i.islower() == False]
    result.sort()
    return list(map(int, result))