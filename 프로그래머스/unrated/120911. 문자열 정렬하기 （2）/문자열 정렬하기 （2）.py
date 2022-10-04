def solution(my_string):
    my_string = my_string.lower()
    string = [i for i in my_string]
    string.sort()
    return "".join(string)