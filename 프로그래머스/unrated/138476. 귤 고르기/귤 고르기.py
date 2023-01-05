def solution(k, tangerine):
    tan_dict = { i : 0 for i in tangerine}
    for j in sorted(tangerine):
        tan_dict[j] += 1

    tan_dict = sorted(tan_dict.items(), key = lambda x : -x[1])
    result = 0
    for i in tan_dict:
        if k >= i[1]:
            k -= i[1]
            result += 1
        elif k != 0:
            k = 0
            result += 1
            break
    return result