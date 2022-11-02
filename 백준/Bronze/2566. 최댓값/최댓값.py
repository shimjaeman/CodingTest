max = 0
row, col = 0, 0
a = [(list(map(int, input().split()))) for _ in range(9)]

for i in range(9):
    for j in range(9):
        if max <= a[i][j] :
            max = a[i][j]
            row, col = i+1, j+1
print(max)
print(row, col)