from itertools import permutations
def solution(k, dungeons):
    fatigue = [list(i) for i in permutations(dungeons, len(dungeons))]
    max_cnt = []
    rot_cnt = 0
    while rot_cnt < len(fatigue):
        new_k = k
        cnt = 0
        for i in range(len(fatigue[rot_cnt])):
            if new_k >= fatigue[rot_cnt][i][0]:
                new_k -= fatigue[rot_cnt][i][1]
                cnt += 1
                if cnt == len(fatigue[rot_cnt]):
                    max_cnt.append(cnt)
            else :
                max_cnt.append(cnt)
                break
        rot_cnt +=1
    
    return max(max_cnt)