def solution(arr):
    arr_min = min(arr)
    a = [i for i in arr if i != arr_min]
    return [-1] if a == [] else a