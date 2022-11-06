n = []
sum = 0
for i in range(5):
    a = int(input())
    n.append(a)
    sum += a
sort_n = sorted(n)
print(sum//5)
print(int(sort_n[2]))