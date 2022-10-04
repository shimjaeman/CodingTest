# 더하고(합치고(함수지정 x : str바꾸고.str(x)의 갯수 새고, [x 값]))
def solution (order):
    return sum(map(lambda x :str(order).count(str(x)),[3,6,9]))
