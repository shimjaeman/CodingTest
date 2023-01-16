def solution(k, m, score):
    # 상태에 따라 1점부터 k점까지의 점수로 분류
    # 한 상자에 사과를 m개씩 담아 포장
    # 가장 낮은 점수가 p점인 경우, 사과 한 상자의 가격은 p * m \
    # 얻을 수 있는 최대 이익을 계산 (그리드?)
    # 상자 단위로만 판매하며, 남는 사과는 패기
    # 이익이 발생하지 않는 경우에는 0을 return 
    # 정렬 => m개 묶기 
    score.sort(reverse=True)
    answer = [[] for i in range((len(score) // m)+1)]
    box_cnt = 0
    movbox = 0
    for i in score:
        if box_cnt == m:
            box_cnt = 0
            movbox +=1
            
        if box_cnt <=m :
            answer[movbox].append(i)
            box_cnt += 1
    
    sort_answer = [sorted(i)[0] * m for i in answer if len(i) == m]
    return sum(sort_answer)