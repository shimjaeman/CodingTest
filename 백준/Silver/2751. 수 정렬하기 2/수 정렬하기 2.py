import sys
input = sys.stdin.readline
a = int(input())
b = []
for i in range(a):
    b.append(int(input()))

b.sort(reverse=False)

for j in b:
    print(j)