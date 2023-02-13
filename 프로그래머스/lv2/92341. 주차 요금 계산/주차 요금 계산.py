import math
def solution(fees, records):
    fees_array = [record.split() for record in records]
    result = {n[1] : 0 for n in fees_array}
    check = dict()
    # 주자 시간 기준 설정
    for p in range(len(fees_array)):
        fees_array[p][0] = int(fees_array[p][0].split(":")[0]) * 60 + int(fees_array[p][0].split(":")[1])
    
    # 주차 요금 계산 
    for park in fees_array:
    # 주자장에 들어온 경우 (IN)
        if park[2] == "IN":
            check[park[1]] = park[0]
    # 주차장에 나가는 경우 (OUT)
        elif park[2] == "OUT":
            park_fee = abs(park[0] - check[park[1]])
            result[park[1]] += park_fee
            check[park[1]] = 0
    # 주차장 나가는 시간이 없는 경우 (23:59 = 1439)
    for ch in check.items():
        if ch[1] != 0:
            end_fee = 1439 - ch[1]
            result[ch[0]] += end_fee
    for n in result.items():
        if n[1] == 0:
            result[n[0]] = 1439
    # 주차 요금 계산 
    for i, j in result.items():
        if int(j) <= fees[0]:
            result[i] = fees[1]
        else :
            result[i] = fees[1] + math.ceil((j - fees[0]) / fees[2]) * fees[3]
    fees_result = [n[1] for n in sorted(result.items())]
    return fees_result