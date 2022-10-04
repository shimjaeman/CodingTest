def solution(order):
    result = 0
    str_ord = str(order)
    len_ord = len(str_ord)
    for i in range(len_ord):
        if str_ord[i] == '3' or str_ord[i] == '6' or str_ord[i] == '9':
            result += 1
    return result