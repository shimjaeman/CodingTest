def solution(array, n):
    sort_array = sorted(array)
    result = [abs(n-i) for i in sort_array]
    min_result = min(result)
    a = result.index(min_result)
    return sort_array[a]
