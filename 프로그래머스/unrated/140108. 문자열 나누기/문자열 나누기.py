def solution(s) :
    answer = 0
    StSp = ["", 1, 0] # 첫글자, 첫글자 횟수, 다른글자 횟수
    new_s = list(s)
    index = 1
    while len(new_s) > 0 :
        # 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없는 경우
        if len(new_s) == index:
            answer += 1
            break
        # 첫글자 읽기
        StSp[0] = new_s[0]
        # 첫글자와 같은 경우
        if StSp[0] == new_s[index]:
            StSp[1] +=1
            index +=1
        # 첫글자와 다른 경우
        else :
            StSp[2] += 1
            # 두 횟수가 같아지는 순간
            if StSp[1] == StSp[2]:
                del new_s[:index+1]
                answer +=1
                StSp[1], StSp[2], index = 1, 0, 1
            # 두 횟수가 달라지는 순간
            else :
                index +=1
            
    return answer