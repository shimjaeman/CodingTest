def solution(number, k):
    list_num = list(number)
    big_num = [list_num.pop(0)]
    for n in list_num:
        if big_num[-1] < n:
            while big_num and big_num[-1] < n and k > 0:
                big_num.pop()
                k -= 1
            big_num.append(n)
        elif k == 0 or big_num[-1] >= n:
            big_num.append(n)
    if k:
        big_num = big_num[:-k]
    result = "".join(big_num)
    return result