def solution(n : int) -> int:
    answer=0
    for i in str(n):
        answer += int(i)
    return answer 