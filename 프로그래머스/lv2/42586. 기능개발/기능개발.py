def solution(progresses, speeds):
    result = []
    for i, (j, k) in enumerate(zip(progresses, speeds)):
        if (100-j) % k != 0:
            result.append(((100-j) // k)+1)
            continue
        a = (100-j) // k
        result.append(a)
    
    for i in range(1, len(result)):
        if result[i-1] > result[i]:
            result[i] = result[i-1]
        else :
            continue
            
    answer = [result.count(n) for n in dict.fromkeys(result)]        
    return answer