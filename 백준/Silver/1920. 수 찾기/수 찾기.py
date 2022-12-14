N = int(input())
A = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

A.sort()
len_A = len(A)

for i in range(M):
    zero = False # 아무것도 발견되지 않은 경우
    target = targets[i]
    start = 0
    end = len_A -1
    while start <= end:
        mid = (start+end)//2
        mid_index = A[mid]
        if mid_index < target :
            start = mid + 1
        elif mid_index > target :
            end = mid -1
        else : # 숫자를 찾은 경우
            zero = True
            break
    if zero:
        print(1)
    else:
        print(0)
            
    