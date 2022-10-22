def count(num):
    val = 1
    for i in range(2, num):
        if num % i == 0:
            val = 0
            break
    if num == 1:
        val = 0
    return val

N = input()
nums = [i for i in map(int, input().split())]
cnt = 0
for num in nums:
    cnt += count(num)
    
print(cnt)