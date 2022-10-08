def solution(my_string, num1, num2):
    a = [i for i in my_string]
    a[num1], a[num2] = a[num2], a[num1]
    return "".join(a)