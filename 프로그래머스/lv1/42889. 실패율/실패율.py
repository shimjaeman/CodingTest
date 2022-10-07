# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

def solution(N, stages):     ###
    # 0) 초기화 작업
    answer = []
    # 비효율 발생을 방지하기 위한 초기화 작업
    fail_dict = {i : 0 for i in range(1, N+1)} # key : stage번호, value : 그 stage 실패율 --> 정렬
    num_people = len(stages) # 이 게임에 시작한 인원 --> 스테이지 가면서 변경
    
    # 1) N스테이지를 돌아가면서~~
    for i in range(1, N+1):
        # 실패자 탐색 : stages.counts ---> 파이썬.메서드
        fail_num = stages.count(i)
        
        # 실패자 계산 ... 단. 참가자 유무에 따라서 다르게 계산!!
        if num_people != 0:
            fail_dict[i] = fail_num / num_people
            num_people -= fail_num # 다음 stage에 참가할 인원 정보 갱신
        else : # 참가자가 없는 경우
            fail_dict[i] = 0
            
    # 2) 이제 계산한 자료를 정리하자 ~~~ (정렬)
    fail_list = sorted(fail_dict.items(), key = lambda x : x[1], reverse = True)
    
    # 3) 문제에서 요구한 사항대로 출력물 제작 --> only 스테이지 번호[list 형태로]
    answer = [info[0] for info in fail_list]
    ###
    return answer