def solution(common):
    # 등차수열 확인
    if common[2]- common[1] == common[1]- common[0]:
        n = common[2]- common[1]
        return common[-1] + (n)
        
    # 등비수열 확인
    if common[2]/common[1]==common[1]/common[0]:
        n = common[2]//common[1]
        return common[-1] * (n)