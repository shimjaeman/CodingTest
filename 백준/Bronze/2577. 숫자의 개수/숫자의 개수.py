a = int(input())
b = int(input())
c = int(input())
d = a * b * c

d = sorted(str(d))
for i in range(10):
    a = d.count(str(i))
    print(a)