# 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.
def solution(A,B):
    A = sorted(A, reverse = False)
    B = sorted(B, reverse = True)
    result = 0
    for i in range(len(A)):
        result += A[i] * B[i]
    return result # 누적된 값이 최소가 되도록 만드는 것