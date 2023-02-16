def solution(n, k):
    answer = []
    line = [i for i in range(1, n+1)]
    while n > 0 :
        # 최대 n 팩토리얼 값 구하기
        max_k = 1
        for i in range(1, n):
            max_k *= i
            
        # 해당 k번째 첫번쨰 값 구하기 
        index = (k-1) // max_k
        answer.append(line[index])
        
        # answer에 포함된 값 제거
        del line[index]
        
        # n 팩토리얼 축소로 k값도 동일하게 축소 
        k = k % max_k
        
        # n 값 제거
        n -= 1
    return answer