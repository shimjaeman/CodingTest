def solution(array):
    answer = []
    ar_len = len(array)
    max_num = 0
    
    for p in range(ar_len):
        if array[p] >= max_num:
            max_num = array[p]
            max_num_index = p
    answer.extend([max_num, max_num_index])
        
    return answer