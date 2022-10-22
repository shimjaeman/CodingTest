N = int(input())

result = []
cnt = 2
while True:
    if N == 1:
        break
    if N % cnt == 0:
        result.append(cnt)
        N = N//cnt
    else :
        cnt += 1

for i in result:
    print(i)