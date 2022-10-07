def solution(num_list, n):
    answer = []
    num_len = len(num_list)
    num = num_list
    
    for i in range(0,num_len,n):
        answer.append([num [i+p] for p in range(n)])
        
    return answer