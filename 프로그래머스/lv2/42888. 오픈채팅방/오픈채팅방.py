def solution(record):
    kakao_ch = {}
    new_record = [i.split(" ") for i in record]
    Process = ["Enter", "Leave", "Change"]
    result = []
    while new_record :
        # 데이터 베이스에 유저 id가 담기지 않은 경우
        if new_record[0][1] not in kakao_ch.keys():
            kakao_ch[new_record[0][1]] = new_record[0][2]
            # enter (처음 들어온 경우는 들어온 경우만 있을테니까)
            if Process[0] == new_record[0][0]:
                result.append([new_record[0][1], "Enter"])
                del new_record[0]
        # 데이터 베이스에 유저 id가 담긴 경우
        else :
            # enter (다시 들어온 경우니 닉네임 확인)
            if Process[0] == new_record[0][0]:
                kakao_ch[new_record[0][1]] = new_record[0][2]
                result.append([new_record[0][1], "Enter"])
                del new_record[0]
            # leave
            elif Process[1] == new_record[0][0]:
                result.append([new_record[0][1], "leave"])
                del new_record[0]
            else :
                kakao_ch[new_record[0][1]] = new_record[0][2]
                del new_record[0]
    message = []
    for n in result:
        if n[1] == "Enter":
            message.append(f"{kakao_ch[n[0]]}님이 들어왔습니다.")
        else :
            message.append(f"{kakao_ch[n[0]]}님이 나갔습니다.")
        
    return message