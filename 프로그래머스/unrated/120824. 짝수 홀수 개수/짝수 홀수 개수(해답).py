# 나는 a = 0, b = 0의 변수를 만들고 최종적으로 [a,b]로 답을 냈으나
# anwer = [0,0]의 변수를 만들고 리스트의 answer[0]와 answer[1]에 숫자를 넣는 식으로 표현하는 것도 있다는 것을 알게되었다.
def solution(num_list):
    answer = [0,0]

    for num in num_list:
        if num % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1

    return answer
