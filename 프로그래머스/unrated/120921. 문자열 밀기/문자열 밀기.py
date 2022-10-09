def solution(A, B):
    cnt = 0
    for i in range(len(A)+1):
        if A == B:
            return cnt
        A = A[-1] + A[0:len(A)-1]
        cnt +=1
    return -1