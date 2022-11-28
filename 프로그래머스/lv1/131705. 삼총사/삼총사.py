def solution(number):
    result = 0
    n_l = len(number)
    for i in range(n_l-2):
        for j in range(i+1, n_l-1):
            for k in range(j+1, n_l):
              if number[i] + number[j] + number[k] == 0:
                result +=1
    return result