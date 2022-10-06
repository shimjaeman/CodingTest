# 실패율 : 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

def solution(N, stages): # N(전체 스테이지의 개수), stages(현재 멈춰있는 스테이지의 번호)
    stage_len = len(stages) # 스테이지에 있는 플레이어 수 
    fail_rate = [0] * N # 실패율 리스트
    fail_count = 0 #  아직 클리어하지 못한 플레이어의 수
    prev_stage = 0 # 이전 스테이지
    
    for i, cur_stage in enumerate(sorted(stages)):
        # 빠져나가는 조건
        if cur_stage == N+1:
            break
        
        # 이전 스테이지와 현재 스테이지의 클리어 여부
        if prev_stage != cur_stage:
            stage_len -= fail_count
            fail_count = 1
            prev_stage = cur_stage
        else :
            fail_count += 1
        fail_rate[cur_stage - 1] = fail_count / stage_len
            
        
    return [id+1 for id, cur in sorted(enumerate(fail_rate), \
                                                   key = lambda x : (-x[1], x[0]))]