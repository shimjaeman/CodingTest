def solution(my_string):
    new_string = "".join(dict.fromkeys(my_string))
    return new_string