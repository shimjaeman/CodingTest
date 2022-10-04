# 딕션어리 자료형으로 표현
# k, v = 사람이름, 그 이름에 대한 사람 수
# 참가를 하면 value +1 / 완주를 하면 value -1
# 마지막에 value == 1인 key가 못들어온 사람

def solution(participant, completion):
    answer =""
    # 0) 자료를 정리할 나의 변수 & 자료형
    people_dict = {}
    # 1) 참가자들을 가지고 리스트 업 : name_count (+)
    for p in participant:
        if p in people_dict: # True : 이미 등록된 이름
            people_dict[p] += 1
        else :
            people_dict[p] = 1
        
    # 2) 완주자에 대한 정리 : name_count (-)
    for p in completion:
        # 1명만 참가 했고, 완주를 했는지
        if people_dict[p] == 1:
            del people_dict[p]
        # 2명 이상 참가를 했고, 완주를 했는지
        else :
            people_dict[p] -= 1
    # 3) 최종 결과 : value == 1인 key가 못들어온 사람
    answer = list(people_dict.keys())[0]
    return str(answer)
        
    