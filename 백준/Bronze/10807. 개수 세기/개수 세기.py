n = input()
a = list(map(int, input().split()))
v = input()
cnt = 0
for i in a:
    if str(i) == v:
        cnt += 1
    else :
        continue
print(cnt)