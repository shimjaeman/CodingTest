# 행과 열의 갯수
n, m = map(int, input().split())

# 첫번째 행렬
A = [list(map(int, input().split())) for _ in range(n)]
# 두번째 행렬
B = [list(map(int, input().split())) for _ in range(n)]

# 행렬 덧셈
result = []
for i in range(n):
    for j in range(m):
        print(A[i][j]+B[i][j], end=" ")
    print()

        