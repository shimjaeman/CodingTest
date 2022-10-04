def solution(num, k):
    cnt = 0
    num_str = str(num)
    len_str = len(num_str)
    for i in range(len_str):
        if num_str[i] == str(k):
            return int(i+1)
        elif num_str[i] != str(k):
            cnt += 1
    if cnt >= len_str:
        return -1