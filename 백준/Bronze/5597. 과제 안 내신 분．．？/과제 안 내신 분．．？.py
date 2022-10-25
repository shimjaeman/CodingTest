result = []
a = [input() for _ in range(28)]
a.sort()
for i in range(1, 31):
    if str(i) in a:
        continue
    else:
        result.append(i)

for i in sorted(result):
    print(i)