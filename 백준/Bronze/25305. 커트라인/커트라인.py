a, b = map(int, input().split())
N = list(map(int, input().split()))
sort_N = sorted(N, reverse = True)
for i in range(len(sort_N)):
    if i == b-1:
        print(sort_N[i])
    