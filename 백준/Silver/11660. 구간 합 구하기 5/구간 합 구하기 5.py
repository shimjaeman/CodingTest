import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[0] * (n+1)]
D = [[0] * (n+1) for _ in range(n+1)]

# A 입력
for i in range(n):
    new = [0] + list(map(int, input().split()))
    A.append(new)
    
# 구간합 
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i-1][j]+D[i][j-1]-D[i-1][j-1]+A[i][j]

# 결과값 출력
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] + D[x1-1][y1-1] - D[x1-1][y2]- D[x2][y1-1]
    print(result)

    
    