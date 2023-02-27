def convert (n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
    
def solution(n, t, m, p):
    n_num_list = [convert(i, n) for i in range(0, t * m)]
    result = ""
    stop_num, order = 0, 1
    for num in n_num_list:
        for game_num in num:
            if stop_num == t:
                break
            elif order % m == p % m:
                result += game_num
                stop_num +=1
            order += 1
    return result