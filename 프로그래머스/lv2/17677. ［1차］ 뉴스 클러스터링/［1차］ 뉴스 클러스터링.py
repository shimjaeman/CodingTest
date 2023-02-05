# 입력으로 들어온 두 문자열의 자카드 유사도를 출력
# 유사도 값은 0에서 1 사이의 실수에 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력
# 영문자로 된 글자 쌍만 유효, 특수 문자가 들어있는 경우는 그 글자 쌍을 삭제
# 대문자와 소문자의 차이는 무시

import re
import math
def solution(str1, str2):
    # 대문자 통일 및 다중집합 원소 제작
    str1 = str1.upper()
    str1 = [[str1[i-1], str1[i]] for i in range(1, len(str1))]
    str2 = str2.upper()
    str2 = [[str2[i-1], str2[i]] for i in range(1, len(str2))]

    # 특수 문자가 들어있는 경우는 그 글자 쌍을 삭제
    new_str1 = []
    for str in str1:
        if re.search("[A-Z]+", str[0]) and re.search("[A-Z]+", str[1]):
            new_str1.append(str)
    new_str2 = []
    for str in str2:
        if re.search("[A-Z]+", str[0]) and re.search("[A-Z]+", str[1]):
            new_str2.append(str)
            
    # intersection
    intersection = []
    temp = new_str2.copy()
    for i in new_str1:
        if i in temp:
            temp.remove(i)
            intersection.append(i)

    # Union = (A + B - n)
    Union = len(new_str1) + len(new_str2) - len(intersection)
    
    # result
    if intersection == 0 or Union == 0:
        return 65536
    else :
        return math.floor(65536 * (len(intersection) / Union))