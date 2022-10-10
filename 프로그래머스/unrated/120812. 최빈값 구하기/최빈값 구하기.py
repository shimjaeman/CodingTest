from collections import Counter

def solution(array):
    mode_dict = Counter(array) # {"1":1,"2":1,"3":3,"4":1}
    values = [v for k, v in mode_dict.items()]
    mode = max(values)
    for k, v in mode_dict.items():
        if values.count(mode) > 1:
            return -1
        if v == mode:
            return k