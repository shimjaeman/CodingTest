import math
def primenumber(x):
    if x == 1:
        return False 
    for i in range (2, int(math.sqrt(x) + 1)):	# 2부터 x의 제곱근까지의 숫자
    	if x % i == 0:		# 나눠떨어지는 숫자가 있으면 소수가 아님
        	return False
    return True		


def solution(n, k):
    cnt = 0
    result = ""
    while n > 0:
        a, b = divmod(n, k)
        result += str(b)
        n = a # k로 나눌 때 몫        
    new_result = result[::-1]
    new_result = new_result.split("0") 
    
    # 소수 판별 함수
    cnt = 0
    for num in new_result:
        if num :
            if primenumber(int(num)) :
                cnt +=1 

    return cnt