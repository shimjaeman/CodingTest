# 입력으로 들어온 두 문자열의 자카드 유사도를 출력
# 유사도 값은 0에서 1 사이의 실수에 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력
# 영문자로 된 글자 쌍만 유효, 특수 문자가 들어있는 경우는 그 글자 쌍을 삭제
# 대문자와 소문자의 차이는 무시
from collections import Counter
def solution(str1, str2):
    # 대문자 통일 및 다중집합 원소 제작
    s1 = Counter([str1[i:i+2].upper() for i in range(len(str1)-1) if str1[i:i+2].isalpha()])
    s2 = Counter([str2[i:i+2].upper() for i in range(len(str2)-1) if str2[i:i+2].isalpha()])
            
    # 유사도 Zero        
    if not s1 and not s2:
        return 65536    
    
    answer = int(float(sum((s1&s2).values()))/float(sum((s1|s2).values())) * 65536)
    return answer