def solution(brown, yellow):
    result = brown + yellow
    answer = [0, 0]
    for i in range(1, result):
        row = i
        col = result // row

        if col > row:
          continue
        
        if ((row-2) * (col-2)) == yellow:
            answer[0] = row
            answer[1] = col
    
    return answer