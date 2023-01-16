def solution(lottos, win_nums):
    # 알아볼 수 없는 번호를 0으로 표기
    # 순서와 상관없이, 당첨 번호와 일치하는 번호가 있으면 맞힌 걸로 인정
    # lottos의 모든 원소는 0 이상 45 이하인 정수
    # lottos의 원소들은 정렬되어 있지 않음
    win_dict = {0 : 6, 1 : 6, 2 : 5, 3 : 4, 4 : 3, 5 :2 , 6:1}
    answer = [0,0]
    min_cnt = 0
    
    # 최저 순위
    for i in lottos :
        if i in win_nums:
            min_cnt +=1
    min_result = win_dict[min_cnt]
    
    # 최대 순위 
    max_cnt = lottos.count(0)
    max_result = win_dict[min_cnt + max_cnt]
    return [max_result, min_result]