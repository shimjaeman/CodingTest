A = int(input())
for i in range(A):
    B,C = list(input().split())
    for j in C:
        print(int(B) * j, end="")
    print()